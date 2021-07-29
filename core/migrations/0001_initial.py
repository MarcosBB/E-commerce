# Generated by Django 3.2.5 on 2021-07-29 20:33

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1, verbose_name='Quantidade')),
                ('dataDaCompra', models.DateField(auto_now_add=True, verbose_name='dataDaCompra')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=90, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
                ('descricao', models.TextField(max_length=1000, verbose_name='Descrição')),
                ('imagemPrincipal', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem Principal')),
                ('imagem1', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem 1')),
                ('imagem2', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem 2')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
