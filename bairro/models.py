from django.db import models
from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,MAX_CHAR_FIELD_NAME_LENGTH



# Create your models here.

class Bairro (models.Model):
    nome = models.CharField(max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"