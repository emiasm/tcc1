from django.db import models
from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,MAX_CHAR_FIELD_NAME_LENGTH
from morador.models import Morador
from imovel.models import Imovel

# Create your models here.

TIPO_ESCOLHA=(
	('Sim','Sim'),
	('Não','Não'),
)

class Visita2 (models.Model):
    imovel = models.ForeignKey(Imovel,on_delete=models.CASCADE)
    motivo_visita = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    quantidade_pessoas = models.IntegerField()
    pessoa_doente = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=TIPO_ESCOLHA)
    pessoa_sintoma = models.IntegerField()
    sintomas = models.TextField()
    data_visita = models.DateField()

    dengue = models.BooleanField()
    dengue_hemorragica = models.BooleanField()
    chikungunya = models.BooleanField()
    zika = models.BooleanField()

    descricao = models.TextField()
    data_adicao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.imovel.morador}"