from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from contentoreslixo.models import ContentorLixo
from sensores.models import DadoSensor

class ContainerDetailsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        container_uuid = self.scope['url_route']['kwargs']['contentor_uuid']
        self.container_uuid = container_uuid
        self.room_group_name = f'container-{container_uuid}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({
            'status' : 'connected to websocket',
        }))
    
    async def disconnect(self, code):
        print(f'connection closed with code: {code}')

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        sensor_distancia = text_data_json['sensor_distancia']
        sensor_umidade = text_data_json['sensor_umidade']
        sensor_temperatura = text_data_json['sensor_temperatura']
        sensor_chuva = text_data_json['sensor_chuva']

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'container_message',
            'sensor_distancia' : sensor_distancia,
            'sensor_umidade' : sensor_umidade,
            'sensor_temperatura' : sensor_temperatura,
            'sensor_chuva' : sensor_chuva,
        })

    async def container_message(self, event):

        await self.save_date_item(event)
       
        await self.send(text_data=json.dumps({
            'status' : 'graficos atualizados com sucesso',
        }))

    @database_sync_to_async
    def create_data_item(self, data):
        try:
           contentor = ContentorLixo.objects.get(id = self.container_uuid)
           return DadoSensor.objects.create(
               contentor = contentor,
                sensor_distancia = data['sensor_distancia'],
                sensor_umidade = data['sensor_umidade'],
                sensor_temperatura = data['sensor_temperatura'],
                sensor_chuva = data['sensor_chuva'])
        except Exception as e:
            print(e)

    async def save_date_item(self, data):
        await self.create_data_item(data)
