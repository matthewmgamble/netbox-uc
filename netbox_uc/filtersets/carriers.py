import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.models import Carrier

__all__ = (
    'CarrierFilterSet',
)


class CarrierFilterSet(NetBoxModelFilterSet):
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant (ID)',
    )

    class Meta:
        model = Carrier
        fields = ('id', 'name', 'slug', 'tenant_id')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(account_number__icontains=value) |
            Q(description__icontains=value)
        )
