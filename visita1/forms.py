from django import forms
from .models import Visita1
from morador.models import Morador

class Visita1Form(forms.ModelForm):

    class Meta:
        model = Visita1
        fields = (
            "morador",
            "caixa_agua",
            "materiais_rodantes",
            "depositos_moveis",
            "depositos_naturais",
            "depositos_fixos",
            "outros_depositos",
            "larvicida",
            "focos",
            "quantidade_l",
            "resumo_visita",
            "data_visita",
        )
        widgets = {
            'larvicida': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'focos': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'resumo_visita': forms.Textarea(attrs={
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

    caixa_agua = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px; color: #022f32 ",
            "type":"radio",
        })
    )
    
    materiais_rodantes = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    depositos_moveis = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    depositos_naturais = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    depositos_fixos = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    outros_depositos = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 25px; height: 25px",
            "type":"radio",
        })
    )

    quantidade_l = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control n",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )
    
