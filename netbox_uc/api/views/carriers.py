from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import CarrierSerializer
from netbox_uc.filtersets import CarrierFilterSet
from netbox_uc.models import Carrier

__all__ = (
    'CarrierViewSet',
)


class CarrierViewSet(NetBoxModelViewSet):
    queryset = Carrier.objects.prefetch_related('tenant', 'tags')
    serializer_class = CarrierSerializer
    filterset_class = CarrierFilterSet
