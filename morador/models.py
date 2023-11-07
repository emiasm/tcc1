from django.db import models
from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,MAX_CHAR_FIELD_NAME_LENGTH


# Create your models here.

TIPO_GENERO=(
	('Masculino','Masculino'),
	('Feminino','Feminino'),
	('Transgênero', 'Transgênero'),
    ('Gênero Neutro', 'Gênero Neutro'),
    ('Não-binário', 'Não-binário'),
    ('Prefiro não responder', 'Prefiro não responder'),
    ('Outro', 'Outro'),
)

class Morador (models.Model):
    nome = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    email = models.EmailField()
    data_nascimento = models.DateField()
    sus = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH)
    cpf = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH)
    genero = models.CharField(max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH, choices=TIPO_GENERO)
    telefone = models.CharField(max_length=SMALL_CHAR_FIELD_NAME_LENGTH)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome.split()[0]} | {self.cpf}"