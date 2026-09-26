from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import AutoAttendantSerializer, CallQueueSerializer
from netbox_uc.filtersets import AutoAttendantFilterSet, CallQueueFilterSet
from netbox_uc.models import AutoAttendant, CallQueue

__all__ = (
    'AutoAttendantViewSet',
    'CallQueueViewSet',
)


class AutoAttendantViewSet(NetBoxModelViewSet):
    queryset = AutoAttendant.objects.prefetch_related(
        'platform', 'site', 'tenant', 'resource_account', 'phone_numbers', 'tags',
    )
    serializer_class = AutoAttendantSerializer
    filterset_class = AutoAttendantFilterSet


class CallQueueViewSet(NetBoxModelViewSet):
    queryset = CallQueue.objects.prefetch_related(
        'platform', 'site', 'tenant', 'resource_account', 'phone_numbers', 'tags',
    )
    serializer_class = CallQueueSerializer
    filterset_class = CallQueueFilterSet
