from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import UCPlatform

__all__ = (
    'UCPlatformSerializer',
)


class UCPlatformSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:ucplatform-detail',
    )

    class Meta:
        model = UCPlatform
        fields = (
            'id', 'url', 'display', 'name', 'slug', 'platform_type',
            'version', 'status', 'description', 'comments', 'tags',
            'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name', 'slug')
