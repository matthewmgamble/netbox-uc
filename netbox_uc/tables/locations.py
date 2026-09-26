import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import EmergencyAddress, VoiceLocation

__all__ = (
    'EmergencyAddressTable',
    'VoiceLocationTable',
)


class EmergencyAddressTable(NetBoxTable):
    name = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    validated = columns.BooleanColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = EmergencyAddress
        fields = (
            'pk', 'id', 'name', 'street', 'city', 'province_state',
            'postal_code', 'country', 'latitude', 'longitude', 'site',
            'validated', 'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'street', 'city', 'province_state', 'country', 'validated',
        )


class VoiceLocationTable(NetBoxTable):
    name = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    location = tables.Column(linkify=True)
    platform = tables.Column(linkify=True)
    emergency_address = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    sync_status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = VoiceLocation
        fields = (
            'pk', 'id', 'name', 'site', 'location', 'platform', 'tenant',
            'emergency_address', 'emergency_callback_number',
            'shared_calling_resource_account', 'sync_status', 'last_synced',
            'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'site', 'platform', 'emergency_address',
        )
