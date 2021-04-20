import django_filters as filters
from . import models


class OrganizationFilter(filters.FilterSet):
    q = filters.CharFilter(label="Buscar uma orgs por login", method="search")
    score = filters.NumberFilter(label="Buscar orgs por score")
    score__gt = filters.NumberFilter(
        label="Buscar orgs por score, maiores que o valor informado",
        field_name='score', lookup_expr='gt')
    score__lt = filters.NumberFilter(
        label="Buscar orgs por score, menores que o valor informado",
        field_name='score', lookup_expr='lt')

    def search(self, queryset, name, value):
        return queryset.filter(login__icontains=value)

    class Meta:
        model = models.Organization
        fields = ['q', 'score']
