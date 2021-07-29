from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('apelido', 'nome', 'sobrenome', 'email')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Informações Pessoais', {'fields': ('apelido','nome', 'sobrenome', 'imagem')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )