from django.urls import path

from .views import IndexView, CarrinhoView, LoginView

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('carrinho/',CarrinhoView.as_view(), name='carrinho'),
    path('login/',LoginView.as_view(), name='login'),
]

