#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#def carrinhoView(request):
#    return render(request, "carrinho.html")

class CarrinhoView(TemplateView):
    template_name = "carrinho.html"