from django import forms
from .models import Bairro



class BairroForm(forms.ModelForm):

    class Meta:
        model = Bairro
        fields = (
            "nome",
        )

    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )