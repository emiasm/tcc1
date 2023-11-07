from django import forms
from .models import Imovel
from morador.models import Morador
from rua.models import Rua
from bairro.models import Bairro


class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = (
            "tipo_propriedade",
            "morador",
            "rua",
            "bairro",
            "numero",
            "referencia",
            "reservatorio",
            "quantidade",
        )
        widgets = {
            'tipo_propriedade': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
        }


    morador = forms.ModelChoiceField(
        queryset=Morador.objects.all(),
        label="Morador",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    rua = forms.ModelChoiceField(
        queryset=Rua.objects.all(),
        label="Rua",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    bairro = forms.ModelChoiceField(
        queryset=Bairro.objects.all(),
        label="Bairro",
        required=True,
        widget=forms.Select(attrs={
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

    referencia = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    reservatorio = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    quantidade = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control n",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )
