from sensores.models import Sensor, DadoSensor
from rest_framework import viewsets
from rest_framework import permissions
from sensores.serializers import SensorSerializer, DadoSensorSerializer

from rest_framework.permissions import IsAuthenticated

class SensorViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DadoSensorViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DadoSensor.objects.all()
    serializer_class = DadoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]