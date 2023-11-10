from django import forms
from .models import Visita2
from imovel.models import Imovel
from morador.models import Morador
from rua.models import Rua
from bairro.models import Bairro


class Visita2Form(forms.ModelForm):
    class Meta:
        model = Visita2
        fields = (
            "morador",
            "motivo_visita",
            "quantidade_pessoas",
            "pessoa_doente",
            "pessoa_sintoma",
            "sintomas",
            "dengue",
            "dengue_hemorragica",
            "chikungunya",
            "zika",
            "descricao",
            "data_visita",
        )
        widgets = {
            'pessoa_doente': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'descricao': forms.Textarea(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'sintomas': forms.Textarea(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'data_visita': forms.TextInput(attrs={
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

    motivo_visita = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    quantidade_pessoas = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control n",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    pessoa_sintoma = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    dengue = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px; color: #022f32 ",
            "type":"radio",
        })
    )
    
    dengue_hemorragica = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    chikungunya = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    zika = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )
    
