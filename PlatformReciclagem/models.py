import uuid
from django.db import models
from django.contrib.auth.models import User

class TipoMaterialReciclavel(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'tipo_material_reciclavel'
        verbose_name_plural = 'tiposmateriaisreciclaveis'
        
    def __str__ (self):
        return self.nome

class ProdutoReciclavel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.ForeignKey(TipoMaterialReciclavel, models.CASCADE, primary_key=True)
    quantidade = models.IntegerField(blank=False)
    preco = models.FloatField(blank=False)
    localizacao = models.CharField(max_length=255, blank=False)
    foto = models.ImageField(upload_to='images/')
    descricao = models.CharField(max_length=255, blank=False)
    vendedor = models.OneToOneField(User, models.CASCADE, primary_key=True)
    estadoColeta = models.BooleanField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'produto_reciclavel'
        verbose_name_plural = 'produtosreciclaveis'
        
    def __str__ (self):
        return self.nome
    
class Transacao(models.Model):
    compradores = models.ManyToManyField(User, primary_key=True)
    vendedores = models.ManyToManyField(User, primary_key=True)
    produtos = models.ManyToManyField(ProdutoReciclavel, models.CASCADE, primary_key=True)
    estado = models.BooleanField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'transacao'
        verbose_name_plural = 'transacoes'
        
    def __str__ (self):
        return self.nome
    
class Carrinho(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE, null=True, blank=True, primary_key=True)
    produtos = models.ManyToManyField(ProdutoReciclavel, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        managed = True
        db_table = 'carrinho'
        verbose_name_plural = 'carrinhos'
        
    def __str__ (self):
        return self.nome