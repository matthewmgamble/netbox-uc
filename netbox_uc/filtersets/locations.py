import django_filters
from django.db.models import Q
from dcim.models import Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import SyncStatusChoices
from netbox_uc.models import EmergencyAddress, UCPlatform, VoiceLocation

__all__ = (
    'EmergencyAddressFilterSet',
    'VoiceLocationFilterSet',
)


class EmergencyAddressFilterSet(NetBoxModelFilterSet):
    validated = django_filters.BooleanFilter()
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label='Site (ID)',
    )

    class Meta:
        model = EmergencyAddress
        fields = ('id', 'name', 'city', 'province_state', 'country', 'validated')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(street__icontains=value) |
            Q(city__icontains=value) |
            Q(postal_code__icontains=value) |
            Q(description__icontains=value)
        )


class VoiceLocationFilterSet(NetBoxModelFilterSet):
    sync_status = django_filters.MultipleChoiceFilter(
        choices=SyncStatusChoices,
    )
    platform_id = django_filters.ModelMultipleChoiceFilter(
        queryset=UCPlatform.objects.all(),
        label='Platform (ID)',
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
        model = VoiceLocation
        fields = ('id', 'name')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )
