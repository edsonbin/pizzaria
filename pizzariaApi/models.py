from django.db import models

class Pizza(models.Model):
    sabor = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=2)
    preco = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

class Cliente(models.Model):
    telefone = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)
    enderecoEntrega = models.CharField(max_length=200)
