from django.db import models
from contentoreslixo.models import ContentorLixo

# Create your models here.

class DadoSensor(models.Model):
    contentor = models.ForeignKey(ContentorLixo, on_delete=models.CASCADE, blank=False)
    sensor_distancia = models.FloatField(default=0)
    sensor_umidade = models.FloatField(default=0)
    sensor_temperatura = models.FloatField(default=0)
    sensor_chuva = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'dado_sensores'
        verbose_name_plural = 'dadosensores'

    def __str__ (self):
        return self.contentor.nome
