from django.urls import path

from .views import IndexView, CarrinhoView

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('carrinho/',CarrinhoView.as_view(), name='carrinho'),
]

