from django.urls import path
from django.conf.urls import url,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^pizzas/$', views.PizzaViewSet.as_view({'get': 'pizza-list'})),
    url(r'^clientes/$', views.ClienteViewSet.as_view({'get':'cliente-list'})),
    url(r'^pedidos/$', views.PedidoViewSet.as_view({'get': 'pedido-list'}))
]