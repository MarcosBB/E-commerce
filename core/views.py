from core.models import Produto
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()

        return context

class CarrinhoView(TemplateView):
    template_name = "carrinho.html"

class LoginView(TemplateView):
    template_name = "login.html"