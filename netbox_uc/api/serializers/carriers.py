from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import Carrier

__all__ = (
    'CarrierSerializer',
)


class CarrierSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:carrier-detail',
    )

    class Meta:
        model = Carrier
        fields = (
            'id', 'url', 'display', 'name', 'slug', 'account_number',
            'support_contact', 'portal_url', 'tenant', 'description',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name', 'slug')
