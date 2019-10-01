from rest_framework import serializers
from .models import Pizza, Cliente, Pedido

class PizzaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pizza
        fields = ('__all__')

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('__all__')

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = ('__all__')