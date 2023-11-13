import django_filters

from .models import Visita2


class Visita2Filter(django_filters.FilterSet):
    morador = django_filters.CharFilter(field_name='morador__nome', lookup_expr='icontains')

    class Meta:
        model = Visita2
        fields = ['morador']