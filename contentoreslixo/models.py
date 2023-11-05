import uuid
from django.db import models

# Create your models here.

class ContentorLixo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    localizacao = models.CharField(max_length=100, blank=False)
    geolocalizacao = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'contentores_lixo'
        verbose_name_plural = 'contentorerslixo'
        
    def __str__ (self):
        return self.nome