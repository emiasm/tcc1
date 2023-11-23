from django.db import models
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Perfil (models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    cpf = models.CharField(blank=True, max_length=255)
    telefone = models.CharField(blank=True, max_length=255)
    cep = models.CharField(blank=True, max_length=255)
    logradouro = models.CharField(blank=True, max_length=255)
    numero = models.CharField(blank=True, max_length=255)
    complemento = models.CharField(blank=True, max_length=255)
    bairro = models.CharField(blank=True, max_length=255)
    cidade = models.CharField(blank=True, max_length=255)
    foto_perfil = models.ImageField(upload_to='static/media/img', null=True, blank=True, default="static/media/img/user.png")