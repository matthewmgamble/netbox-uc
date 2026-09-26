from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import ResourceAccountSerializer
from netbox_uc.filtersets import ResourceAccountFilterSet
from netbox_uc.models import ResourceAccount

__all__ = (
    'ResourceAccountViewSet',
)


class ResourceAccountViewSet(NetBoxModelViewSet):
    queryset = ResourceAccount.objects.prefetch_related('platform', 'site', 'tenant', 'phone_number', 'tags')
    serializer_class = ResourceAccountSerializer
    filterset_class = ResourceAccountFilterSet
