from sensores.models import DadoSensor
from rest_framework import viewsets
from rest_framework import permissions
from sensores.serializers import DadoSensorSerializer

class DadoSensorViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DadoSensor.objects.all()
    serializer_class = DadoSensorSerializer
    permission_classes = [permissions.AllowAny]