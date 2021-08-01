from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.views.decorators.http import require_POST
from core.models import Produto

from .carrinho import Carrinho
from .forms import AdicionarProdutoAoCarrinhoForm



@require_POST
def carrinho_adicionar(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)

    form = AdicionarProdutoAoCarrinhoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.adicionar(
            produto=produto,
            quantidade=cd["quantidade"],
            override_quantidade=cd["override"]
        )

    return redirect("carrinho")

@require_POST
def carrinho_remover(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remover(produto)

    return redirect("carrinho")

def carrinhoView(request):
    carrinho = Carrinho(request)
    return render(request, "carrinho.html", {"carrinho": carrinho})