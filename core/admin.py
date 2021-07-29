from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco' ,'modificado', 'ativo')

