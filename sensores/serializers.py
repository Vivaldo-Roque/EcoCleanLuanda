from sensores.models import DadoSensor
from rest_framework import serializers


class DadoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadoSensor
        fields = '__all__'