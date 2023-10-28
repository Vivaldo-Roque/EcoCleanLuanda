from django.contrib import admin
from .models import Sensor, DadoSensor

# Registar aqui as classes

admin.site.register(DadoSensor)
admin.site.register(Sensor)
