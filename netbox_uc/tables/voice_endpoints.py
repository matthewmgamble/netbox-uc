import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import VoiceEndpoint

__all__ = (
    'VoiceEndpointTable',
)


class VoiceEndpointTable(NetBoxTable):
    name = tables.Column(linkify=True)
    endpoint_type = columns.ChoiceFieldColumn(verbose_name='Type')
    status = columns.ChoiceFieldColumn()
    platform = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    phone_number = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    sync_status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = VoiceEndpoint
        fields = (
            'pk', 'id', 'name', 'endpoint_type', 'status', 'platform',
            'site', 'device', 'interface', 'phone_number', 'user_account',
            'resource_account', 'manufacturer', 'model', 'serial_number',
            'mac_address', 'firmware', 'tenant', 'sync_status', 'last_synced',
            'last_seen', 'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'endpoint_type', 'status', 'platform', 'site',
            'phone_number', 'mac_address',
        )
