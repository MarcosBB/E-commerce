from decimal import Decimal
from core.models import Produto
import copy

from .forms import AdicionarProdutoAoCarrinhoForm

class Carrinho():
    def __init__(self, request):
        if request.session.get("carrinho") is None:
            request.session["carrinho"] = {}

        self.session = request.session
        self.carrinho = request.session["carrinho"]
    
    def __iter__(self):
        carrinho = copy.deepcopy(self.carrinho)
        produtos = Produto.objects.filter(id__in = carrinho)
        for produto in produtos:
            carrinho[str(produto.id)]["produto"] = produto

        for item in carrinho.values():
            item["preco"] = Decimal(item["preco"])
            item["preco_total"] = item["preco"] * item["quantidade"]
            item["update_quantidade_form"] = AdicionarProdutoAoCarrinhoForm(
                initial={"quantidade": item["quantidade"], "override": True}
            )
            yield item

    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def adicionar (self, produto, quantidade = 1, override_quantidade = False):
        produto_id = str(produto.id)

        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {
                "quantidade": 0,
                "preco": str(produto.preco),
            }
        
        if override_quantidade:
            self.carrinho[produto_id]["quantidade"] = quantidade

        else:
            self.carrinho[produto_id]["quantidade"] += quantidade

        self.carrinho[produto_id]["quantidade"] = min(20, self.carrinho[produto_id]["quantidade"])

        self.salvar()

    def remover (self, produto):
        produto_id = str(produto.id)

        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()

    def get_preco_total(self):
        return sum(
            Decimal(item["preco"]) * item["quantidade"] for item in self.carrinho.values()
        )
 
    def salvar (self):
        self.session.modified = True

    


