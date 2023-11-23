from django import forms
from .models import Rua
from bairro.models import Bairro



class RuaForm(forms.ModelForm):

    class Meta:
        model = Rua
        fields = (
            "nome",
            "bairro",
            "tipo_rua",
        )
        widgets = {
            'tipo_rua': forms.Select(attrs={
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
    bairro = forms.ModelChoiceField(
        queryset=Bairro.objects.all(),
        label="Bairro",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )