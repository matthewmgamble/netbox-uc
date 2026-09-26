from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import NumberRangeSerializer
from netbox_uc.filtersets import NumberRangeFilterSet
from netbox_uc.models import NumberRange

__all__ = (
    'NumberRangeViewSet',
)


class NumberRangeViewSet(NetBoxModelViewSet):
    queryset = NumberRange.objects.prefetch_related('carrier', 'site', 'tenant', 'tags')
    serializer_class = NumberRangeSerializer
    filterset_class = NumberRangeFilterSet
