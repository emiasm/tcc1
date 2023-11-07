from django.db import models
from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,MAX_CHAR_FIELD_NAME_LENGTH
from morador.models import Morador
from imovel.models import Imovel

# Create your models here.

TIPO_ESCOLHA=(
	('Biológico','Biológico'),
	('Químico','Químico'),
    ('Nenhum','Nenhum'),
)

TIPO_FOCOS=(
	('Não há focos','Não há focos'),
	('Tem água parada, mas sem a presença de mosquitos','Tem água parada, mas sem a presença de mosquitos'),
    ('Água parada e presença de mosquitos','Água parada e presença de mosquitos'),
)


class Visita1 (models.Model):
    morador = models.ForeignKey(Morador,on_delete=models.CASCADE)

    caixa_agua = models.BooleanField()
    materiais_rodantes = models.BooleanField()
    depositos_moveis = models.BooleanField()
    depositos_naturais = models.BooleanField()
    depositos_fixos = models.BooleanField()
    outros_depositos = models.BooleanField()

    larvicida = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=TIPO_ESCOLHA)
    quantidade_l = models.IntegerField()
    focos = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=TIPO_FOCOS)
    resumo_visita = models.TextField()
    data_visita = models.DateField()
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.morador}"