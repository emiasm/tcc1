import django_filters

from .models import Visita1


class Visita1Filter(django_filters.FilterSet):
    morador = django_filters.CharFilter(field_name='morador__nome', lookup_expr='icontains')

    class Meta:
        model = Visita1
        fields = ['morador']