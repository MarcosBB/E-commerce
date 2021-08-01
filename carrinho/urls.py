from django.urls import path
from .views import carrinhoView, carrinho_remover, carrinho_adicionar

urlpatterns = [
    path("", carrinhoView, name="carrinho"),
    path("adicionar/<int:produto_id>/", carrinho_adicionar, name="adicionar"),
    path("remover/<int:produto_id>/", carrinho_remover, name="remover"),
]
