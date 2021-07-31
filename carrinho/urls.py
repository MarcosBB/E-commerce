from django.urls import path
from .views import CarrinhoView

urlpatterns = [
    path("", CarrinhoView.as_view(), name="carrinho"),
]
