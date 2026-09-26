from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import EmergencyAddress, VoiceLocation

__all__ = (
    'EmergencyAddressSerializer',
    'VoiceLocationSerializer',
)


class EmergencyAddressSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:emergencyaddress-detail',
    )

    class Meta:
        model = EmergencyAddress
        fields = (
            'id', 'url', 'display', 'name', 'street', 'city',
            'province_state', 'postal_code', 'country',
            'latitude', 'longitude', 'site',
            'validated', 'external_id', 'sync_status', 'last_synced',
            'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')


class VoiceLocationSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:voicelocation-detail',
    )

    class Meta:
        model = VoiceLocation
        fields = (
            'id', 'url', 'display', 'name', 'site', 'location', 'platform',
            'tenant', 'emergency_address', 'emergency_callback_number',
            'shared_calling_resource_account', 'external_id',
            'sync_status', 'last_synced', 'description', 'comments',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')
