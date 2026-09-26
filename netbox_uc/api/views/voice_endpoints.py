from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import VoiceEndpointSerializer
from netbox_uc.filtersets import VoiceEndpointFilterSet
from netbox_uc.models import VoiceEndpoint

__all__ = (
    'VoiceEndpointViewSet',
)


class VoiceEndpointViewSet(NetBoxModelViewSet):
    queryset = VoiceEndpoint.objects.prefetch_related(
        'platform', 'site', 'tenant', 'device', 'interface',
        'phone_number', 'user_account', 'resource_account',
        'manufacturer', 'tags',
    )
    serializer_class = VoiceEndpointSerializer
    filterset_class = VoiceEndpointFilterSet
