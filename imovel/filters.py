import django_filters

from .models import Imovel


class ImovelFilter(django_filters.FilterSet):
    morador = django_filters.CharFilter(field_name='morador__nome', lookup_expr='icontains')

    class Meta:
        model = Imovel
        fields = ['morador']