from django.db import models
from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,MAX_CHAR_FIELD_NAME_LENGTH
from bairro.models import Bairro

# Create your models here.

TIPO_RUA=(
	('Urbana','Urbana'),
	('Rural','Rural'),
)

class Rua (models.Model):
    nome = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    tipo_rua = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH, choices=TIPO_RUA)
    bairro = models.ForeignKey(Bairro,on_delete=models.CASCADE)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} | {self.tipo_rua}"