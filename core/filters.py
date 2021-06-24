from django_filters import CharFilter, rest_framework as filters

from core.models import Organization


class OrganizationFilter(filters.FilterSet):

    name = CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )

    class Meta:
        model = Organization
        fields = [
            'name'
        ]
