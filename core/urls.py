from django.urls import path

from .views import IndexView, HistoricoView

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('historico/',HistoricoView.as_view(), name='historico'),
]


