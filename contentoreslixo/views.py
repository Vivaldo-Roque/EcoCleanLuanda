from contentoreslixo.models import ContentorLixo
from rest_framework import viewsets
from rest_framework import permissions
from contentoreslixo.serializers import ContetorLixoSerializer

from rest_framework.permissions import IsAuthenticated

class ContentorLixoViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ContentorLixo.objects.all()
    serializer_class = ContetorLixoSerializer
    permission_classes = [permissions.IsAuthenticated]