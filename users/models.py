from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

TIPO_CARGO=(
	('Agente de Saúde','Agente de Saúde'),
	('Agente de Endemias','Agente de Endemias'),
)


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    cpf = models.CharField(_("Number of CPF"), blank=True, max_length=255)
    email = models.EmailField(_("Email"), blank=True)
    telefone = models.CharField(_("Number of Telefone"), blank=True, max_length=255)
    cep = models.CharField(_("Number of CEP"), blank=True, max_length=255)
    logradouro = models.CharField(_("Logradouro"), blank=True, max_length=255)
    numero = models.CharField(_("Number of Casa"), blank=True, max_length=255)
    complemento = models.CharField(_("Complemento"), blank=True, max_length=255)
    bairro = models.CharField(_("Bairro"), blank=True, max_length=255)
    cidade = models.CharField(_("Cidade"), blank=True, max_length=255)
    cargo = models.CharField(_("Cargo"), blank=True, max_length=255, choices=TIPO_CARGO)
    foto_perfil = models.ImageField(upload_to='static/media/img', null=True, blank=True, default="static/media/img/user.png")
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    data_adicao = models.DateTimeField(auto_now_add=True)
    