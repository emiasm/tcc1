import django_filters
from django import forms
from .models import Visita1


class Visita1Filter(django_filters.FilterSet):
    morador = django_filters.CharFilter(field_name='imovel__morador__nome', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;border-start-start-radius: 5px;border-end-end-radius: 0px; border-end-start-radius: 5px;border-start-end-radius: 0px;",
        "placeholder": "Procurar por morador"
    }))

    class Meta:
        model = Visita1
        fields = ['imovel']