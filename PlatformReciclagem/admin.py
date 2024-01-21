from django.contrib import admin
from PlatformReciclagem.models import Venda, Vendedor, Comprador

# Register your models here.

admin.site.register(Vendedor)
admin.site.register(Comprador)
admin.site.register(Venda)