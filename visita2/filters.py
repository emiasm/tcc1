import django_filters
from django import forms
from .models import Visita2


class Visita2Filter(django_filters.FilterSet):
    morador = django_filters.CharFilter(field_name='morador__nome', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;border-start-start-radius: 5px;border-end-end-radius: 0px; border-end-start-radius: 5px;border-start-end-radius: 0px;",
        "placeholder": "Procurar por morador"
    }))

    class Meta:
        model = Visita2
        fields = ['morador']