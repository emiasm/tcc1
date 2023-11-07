from django.db import models
from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,MAX_CHAR_FIELD_NAME_LENGTH
from rua.models import Rua
from bairro.models import Bairro
from morador.models import Morador



# Create your models here.

TIPO_PROPRIEDADE=(
	('Residencial','Residencial'),
	('Comercial','Comercial'),
	('Industrial', 'Industrial'),
)

class Imovel (models.Model):
    tipo_propriedade = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH, choices=TIPO_PROPRIEDADE)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    rua = models.ForeignKey(Rua,on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro,on_delete=models.CASCADE)
    numero = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    referencia = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    reservatorio = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH)
    quantidade = models.IntegerField()
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_propriedade} | {self.numero} | {self.rua} | {self.bairro}"