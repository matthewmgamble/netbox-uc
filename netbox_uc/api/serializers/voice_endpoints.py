from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import VoiceEndpoint

__all__ = (
    'VoiceEndpointSerializer',
)


class VoiceEndpointSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:voiceendpoint-detail',
    )

    class Meta:
        model = VoiceEndpoint
        fields = (
            'id', 'url', 'display', 'name', 'endpoint_type', 'platform',
            'site', 'tenant', 'device', 'interface', 'phone_number',
            'user_account', 'resource_account', 'manufacturer', 'model',
            'serial_number', 'mac_address', 'firmware', 'status',
            'last_seen', 'external_id', 'sync_status', 'last_synced',
            'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name', 'endpoint_type')
