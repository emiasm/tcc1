from django import forms
from .models import Morador
from decimal import Decimal

class MoradorForm(forms.ModelForm):

    class Meta:
        model = Morador
        fields = (
            "nome",
            "email",
            "data_nascimento",
            "sus",
            "cpf",
            "genero",
            "telefone",
        )
        widgets = {
            'genero': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'data_nascimento': forms.TextInput(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
        }
        

    nome = forms.CharField(
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

    # data_nascimento = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "style": "height:45px; border:none; border-radius:10px"
    #     })
    # )

    sus = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control n",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control cpf",
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
