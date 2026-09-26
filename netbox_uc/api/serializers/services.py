from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_uc.models import AutoAttendant, CallQueue

__all__ = (
    'AutoAttendantSerializer',
    'CallQueueSerializer',
)


class AutoAttendantSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:autoattendant-detail',
    )

    class Meta:
        model = AutoAttendant
        fields = (
            'id', 'url', 'display', 'name', 'platform', 'site', 'tenant',
            'resource_account', 'phone_numbers', 'status', 'timezone',
            'language', 'external_id', 'sync_status', 'last_synced',
            'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')


class CallQueueSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_uc-api:callqueue-detail',
    )

    class Meta:
        model = CallQueue
        fields = (
            'id', 'url', 'display', 'name', 'platform', 'site', 'tenant',
            'resource_account', 'phone_numbers', 'status', 'external_id',
            'sync_status', 'last_synced', 'description', 'comments',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')
