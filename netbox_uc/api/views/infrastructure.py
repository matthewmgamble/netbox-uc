from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import (
    SessionBorderControllerSerializer, SIPTrunkEndpointSerializer, SIPTrunkSerializer,
)
from netbox_uc.filtersets import (
    SessionBorderControllerFilterSet, SIPTrunkEndpointFilterSet, SIPTrunkFilterSet,
)
from netbox_uc.models import SessionBorderController, SIPTrunk, SIPTrunkEndpoint

__all__ = (
    'SIPTrunkViewSet',
    'SIPTrunkEndpointViewSet',
    'SessionBorderControllerViewSet',
)


class SIPTrunkViewSet(NetBoxModelViewSet):
    queryset = SIPTrunk.objects.prefetch_related('carrier', 'platform', 'site', 'tenant', 'tags')
    serializer_class = SIPTrunkSerializer
    filterset_class = SIPTrunkFilterSet


class SIPTrunkEndpointViewSet(NetBoxModelViewSet):
    queryset = SIPTrunkEndpoint.objects.prefetch_related('sip_trunk', 'tags')
    serializer_class = SIPTrunkEndpointSerializer
    filterset_class = SIPTrunkEndpointFilterSet


class SessionBorderControllerViewSet(NetBoxModelViewSet):
    queryset = SessionBorderController.objects.prefetch_related(
        'device', 'platform', 'tenant', 'sip_trunks', 'tags',
    )
    serializer_class = SessionBorderControllerSerializer
    filterset_class = SessionBorderControllerFilterSet
