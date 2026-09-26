from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import UCPlatformSerializer
from netbox_uc.filtersets import UCPlatformFilterSet
from netbox_uc.models import UCPlatform

__all__ = (
    'UCPlatformViewSet',
)


class UCPlatformViewSet(NetBoxModelViewSet):
    queryset = UCPlatform.objects.prefetch_related('tags')
    serializer_class = UCPlatformSerializer
    filterset_class = UCPlatformFilterSet
