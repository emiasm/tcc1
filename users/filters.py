import django_filters
from django import forms

from .models import User


class UsersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user__name', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;border-start-start-radius: 5px;border-end-end-radius: 0px; border-end-start-radius: 5px;border-start-end-radius: 0px;",
        "placeholder": "Procurar por nome"
    }))

    class Meta:
        model = User
        fields = ['name']
