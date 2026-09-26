from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import ResourceAccount

__all__ = (
    'ResourceAccountSerializer',
)


class ResourceAccountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:resourceaccount-detail',
    )

    class Meta:
        model = ResourceAccount
        fields = (
            'id', 'url', 'display', 'display_name', 'user_principal_name',
            'object_id', 'resource_account_type', 'platform', 'site',
            'tenant', 'phone_number', 'status', 'external_id',
            'sync_status', 'last_synced', 'description', 'comments',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'display_name', 'user_principal_name')
