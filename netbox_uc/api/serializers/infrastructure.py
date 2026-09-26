from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import SessionBorderController, SIPTrunk, SIPTrunkEndpoint

__all__ = (
    'SIPTrunkSerializer',
    'SIPTrunkEndpointSerializer',
    'SessionBorderControllerSerializer',
)


class SIPTrunkSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:siptrunk-detail',
    )

    class Meta:
        model = SIPTrunk
        fields = (
            'id', 'url', 'display', 'name', 'carrier', 'platform', 'site',
            'tenant', 'status', 'direction', 'signaling_protocol',
            'media_protocol', 'external_id', 'description', 'comments',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')


class SIPTrunkEndpointSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:siptrunkendpoint-detail',
    )

    class Meta:
        model = SIPTrunkEndpoint
        fields = (
            'id', 'url', 'display', 'sip_trunk', 'fqdn_or_ip', 'port',
            'protocol', 'priority', 'description',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'fqdn_or_ip', 'port', 'priority')


class SessionBorderControllerSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:sessionbordercontroller-detail',
    )

    class Meta:
        model = SessionBorderController
        fields = (
            'id', 'url', 'display', 'name', 'device', 'platform', 'tenant',
            'role', 'status', 'sip_trunks', 'external_id', 'description',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')
