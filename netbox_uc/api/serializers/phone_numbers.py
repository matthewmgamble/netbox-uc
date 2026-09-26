from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import PhoneNumber

__all__ = (
    'PhoneNumberSerializer',
)


class PhoneNumberSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:phonenumber-detail',
    )

    class Meta:
        model = PhoneNumber
        fields = (
            'id', 'url', 'display', 'number', 'extension', 'status',
            'number_type', 'carrier', 'site', 'tenant', 'platform',
            'sip_trunk', 'assigned_object_type', 'assigned_object_id',
            'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'number', 'status')
