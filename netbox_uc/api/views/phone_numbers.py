from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import PhoneNumberSerializer
from netbox_uc.filtersets import PhoneNumberFilterSet
from netbox_uc.models import PhoneNumber

__all__ = (
    'PhoneNumberViewSet',
)


class PhoneNumberViewSet(NetBoxModelViewSet):
    queryset = PhoneNumber.objects.prefetch_related('carrier', 'site', 'tenant', 'platform', 'tags')
    serializer_class = PhoneNumberSerializer
    filterset_class = PhoneNumberFilterSet
