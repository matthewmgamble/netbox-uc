import django_filters
from django.db.models import Q
from dcim.models import Manufacturer, Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import SyncStatusChoices, VoiceEndpointStatusChoices, VoiceEndpointTypeChoices
from netbox_uc.models import UCPlatform, VoiceEndpoint

__all__ = (
    'VoiceEndpointFilterSet',
)


class VoiceEndpointFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=VoiceEndpointStatusChoices,
    )
    endpoint_type = django_filters.MultipleChoiceFilter(
        choices=VoiceEndpointTypeChoices,
    )
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
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label='Manufacturer (ID)',
    )

    class Meta:
        model = VoiceEndpoint
        fields = ('id', 'name', 'endpoint_type', 'status', 'mac_address', 'serial_number')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(serial_number__icontains=value) |
            Q(mac_address__icontains=value) |
            Q(description__icontains=value)
        )
