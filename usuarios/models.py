from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, models.CASCADE, primary_key=True)
    primeiro_nome = models.CharField(max_length=50, blank=False)
    ultimo_nome = models.CharField(max_length=50, blank=False)
    telefone = models.CharField(max_length=50, blank=False)
    morada = models.CharField(max_length=50, blank=False)

    class Meta:
        managed = True
        db_table = 'perfis'
        verbose_name_plural = 'Perfis'