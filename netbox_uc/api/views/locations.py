from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import EmergencyAddressSerializer, VoiceLocationSerializer
from netbox_uc.filtersets import EmergencyAddressFilterSet, VoiceLocationFilterSet
from netbox_uc.models import EmergencyAddress, VoiceLocation

__all__ = (
    'EmergencyAddressViewSet',
    'VoiceLocationViewSet',
)


class EmergencyAddressViewSet(NetBoxModelViewSet):
    queryset = EmergencyAddress.objects.prefetch_related('site', 'tags')
    serializer_class = EmergencyAddressSerializer
    filterset_class = EmergencyAddressFilterSet


class VoiceLocationViewSet(NetBoxModelViewSet):
    queryset = VoiceLocation.objects.prefetch_related(
        'site', 'location', 'platform', 'tenant', 'emergency_address',
        'emergency_callback_number', 'shared_calling_resource_account', 'tags',
    )
    serializer_class = VoiceLocationSerializer
    filterset_class = VoiceLocationFilterSet
