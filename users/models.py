from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

TIPO_CARGO=(
	('Agente de Saúde','Agente de Saúde'),
	('Agente de Endemias','Agente de Endemias'),
)


class User(AbstractUser):
    email = models.EmailField(blank=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    cargo = models.CharField(_("Cargo"), blank=True, max_length=255, choices=TIPO_CARGO)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    data_adicao = models.DateTimeField(auto_now_add=True)
    
    