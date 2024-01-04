from django.db import models

class Vendedor(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    telefone = models.IntegerField(blank=False)
    provincia = models.CharField(max_length = 50, blank=False)
    endereco = models.CharField(max_length = 100, blank=False)
    tipo_material_reciclavel = models.CharField(50, blank=False)
    quantidade = models.IntegerField(max_length = 50, blank=False)
    descricao = models.CharField(max_length = 500, blank=False)
    peso_total = models.IntegerField(max_length = 50, blank=False)

    class Meta:
        managed = True
        db_table = 'vendedor'
        verbose_name_plural = 'vendedores'
        
    def __str__ (self):
        return self.nome_completo

class Comprador(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    telefone = models.IntegerField(blank=False)
    provincia = models.CharField(max_length = 50, blank=False)
    endereco = models.CharField(max_length = 100, blank=False)
    tipo_material_reciclavel = models.CharField(50, blank=False)
    descricao = models.CharField(max_length = 500, blank=False)
    quantidade_desejada = models.IntegerField(max_length = 50, blank=False)

    class Meta:
        managed = True
        db_table = 'comprador'
        verbose_name_plural = 'compradores'
        
    def __str__ (self):
        return self.nome_completo
    
class Venda(models.Model):
    comprador = models.ManyToManyField(Comprador, blank=False)
    vendedor = models.ManyToManyField(Vendedor, blank=False)

    class Meta:
        managed = True
        db_table = 'venda'
        verbose_name_plural = 'vendas'