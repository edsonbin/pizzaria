from django.shortcuts import render

from django.http import HttpResponse

from .models import Pizza, Cliente, Pedido
from rest_framework import viewsets
from .serializers import PizzaSerializer, ClienteSerializer, PedidoSerializer


def index(request):
    return HttpResponse("Oi.")

class PizzaViewSet(viewsets.ModelViewSet):

    queryset = Pizza.objects.all().order_by('-sabor')
    serializer_class = PizzaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer