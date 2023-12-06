import django_filters
from django import forms

from .models import Bairro


class BairroFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;border-start-start-radius: 5px;border-end-end-radius: 0px; border-end-start-radius: 5px;border-start-end-radius: 0px;",
        "placeholder": "Procurar por nome"
    }))

    class Meta:
        model = Bairro
        fields = ['nome']
