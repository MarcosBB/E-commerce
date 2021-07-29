from django.db import models
from stdimage.models import StdImageField
import uuid
from django.contrib.auth import get_user_model

# Create your models here.
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
'''

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome + " " + self.sobrenome
'''

class Produto(Base):
    nome = models.CharField('Nome', max_length=90)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    descricao = models.TextField('Descrição', max_length=1000)
    imagemPrincipal = StdImageField('Imagem Principal', upload_to=get_file_path, variations={'thumb': {'width': 210, 'height': 159, 'crop': True}})
    imagem1 = StdImageField('Imagem 1', upload_to=get_file_path)
    imagem2 = StdImageField('Imagem 2', upload_to=get_file_path)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome 

class Compra(models.Model):
    produtoId = models.ForeignKey("core.Produto", verbose_name=("Produto"), on_delete=models.CASCADE)
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade', default=1)
    dataDaCompra = models.DateField('dataDaCompra', auto_now_add=True)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

