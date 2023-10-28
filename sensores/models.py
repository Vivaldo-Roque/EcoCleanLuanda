from django.db import models
from contentoreslixo.models import ContentorLixo

# Create your models here.

class Sensor(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = True
        db_table = 'sensores'
        verbose_name_plural = 'sensores'

    def __str__ (self):
        return self.nome

class DadoSensor(models.Model):
    contentor = models.ForeignKey(ContentorLixo, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    dado = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'dado_sensores'
        verbose_name_plural = 'dadosensores'

    def __str__ (self):
        return self.contentor.nome
