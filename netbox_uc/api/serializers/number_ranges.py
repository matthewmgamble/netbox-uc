from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import NumberRange

__all__ = (
    'NumberRangeSerializer',
)


class NumberRangeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:numberrange-detail',
    )
    total_numbers = serializers.IntegerField(read_only=True)
    assigned_count = serializers.IntegerField(read_only=True)
    available_count = serializers.IntegerField(read_only=True)
    reserved_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = NumberRange
        fields = (
            'id', 'url', 'display', 'name', 'start_number', 'end_number',
            'carrier', 'status', 'site', 'tenant',
            'total_numbers', 'assigned_count', 'available_count', 'reserved_count',
            'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')
