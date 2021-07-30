from django.urls import path

from .views import IndexView, CarrinhoView,  HistoricoView

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('carrinho/',CarrinhoView.as_view(), name='carrinho'),
    path('historico/',HistoricoView.as_view(), name='historico'),
]


