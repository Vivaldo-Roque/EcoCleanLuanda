from django.db import models

# Create your models here.

class ContentorLixo(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    localizacao = models.CharField(max_length=100, blank=False)
    geolocalizacao = models.CharField(max_length=255, blank=False)

    class Meta:
        managed = True
        db_table = 'contentores_lixo'
        verbose_name_plural = 'contentorerslixo'
        
    def __str__ (self):
        return self.nome