from django.contrib import admin

from .models import Pizza,Cliente,Pedido

admin.site.register(Pizza)
admin.site.register(Cliente)
admin.site.register(Pedido)