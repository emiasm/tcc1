from django import forms
from .models import Perfil
from decimal import Decimal


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = (
            "cpf", "telefone", "cep", "logradouro", "numero", "complemento", "bairro", "cidade","foto_perfil","name","email"
        )
        widgets = {
            'foto_perfil': forms.FileInput(attrs={
                'class': 'form-control',
                "style":"height:45px; border:none; border-radius:10px",
            })
        }

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control cpf",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    cep = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control cep",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )


    logradouro = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    numero = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control n",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    complemento = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    bairro = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    cidade = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))

    telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control tel",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )