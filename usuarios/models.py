from django.db import models
import uuid
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser, BaseUserManager

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O nome de e-mail é obrigatório!')

        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    apelido = models.CharField('Apelido', max_length=100, unique=True)
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    is_staff = models.BooleanField('Membro da equipe', default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['apelido','nome', 'sobrenome', 'imagem']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
