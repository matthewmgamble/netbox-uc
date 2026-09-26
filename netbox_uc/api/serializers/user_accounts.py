from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import UserAccount

__all__ = (
    'UserAccountSerializer',
)


class UserAccountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:useraccount-detail',
    )

    class Meta:
        model = UserAccount
        fields = (
            'id', 'url', 'display', 'display_name', 'user_principal_name',
            'external_id', 'platform', 'phone_number', 'extension',
            'site', 'tenant', 'status', 'description', 'comments',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'display_name', 'user_principal_name')
