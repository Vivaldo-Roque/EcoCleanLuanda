from contentoreslixo.models import ContentorLixo
from rest_framework import serializers

class ContetorLixoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentorLixo
        fields = '__all__'
