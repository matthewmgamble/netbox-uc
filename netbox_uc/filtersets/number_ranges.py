import django_filters
from django.db.models import Q
from dcim.models import Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import NumberRangeStatusChoices
from netbox_uc.models import Carrier, NumberRange

__all__ = (
    'NumberRangeFilterSet',
)


class NumberRangeFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=NumberRangeStatusChoices,
    )
    carrier_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Carrier.objects.all(),
        label='Carrier (ID)',
    )
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label='Site (ID)',
    )
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant (ID)',
    )

    class Meta:
        model = NumberRange
        fields = ('id', 'name', 'status')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(start_number__icontains=value) |
            Q(end_number__icontains=value) |
            Q(description__icontains=value)
        )
