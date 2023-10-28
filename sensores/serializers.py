from sensores.models import DadoSensor, Sensor
from rest_framework import serializers


class DadoSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadoSensor
        fields = '__all__'

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'