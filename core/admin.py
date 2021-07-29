from django.contrib import admin
from .models import Produto, Compra

@admin.register(Produto)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco' ,'modificado', 'ativo')


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('produtoId', 'quantidade', '_autor')
    exclude = ['autor'] # Exclui o campo usuario da página admin no formulario de compra

    # Exibindo nome do usuário completo
    def _autor(self, instance):
        return f'{instance.autor.apelido}'

    # Mostrando apenas as compras do usuário logado
    def get_queryset(self, request):
        qs = super(CompraAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    # Permitindo que apenas o usuário logado faça compras no seu nome
    def save_model(self, request, obj, form, change) :
        obj.autor = request.user
        super().save_model(request, obj, form, change)

