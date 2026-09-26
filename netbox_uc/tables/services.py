import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import AutoAttendant, CallQueue

__all__ = (
    'AutoAttendantTable',
    'CallQueueTable',
)


class AutoAttendantTable(NetBoxTable):
    name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    platform = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    resource_account = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    sync_status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = AutoAttendant
        fields = (
            'pk', 'id', 'name', 'status', 'platform', 'site',
            'resource_account', 'tenant', 'timezone', 'language',
            'sync_status', 'last_synced', 'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'status', 'platform', 'site', 'resource_account',
        )


class CallQueueTable(NetBoxTable):
    name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    platform = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    resource_account = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    sync_status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = CallQueue
        fields = (
            'pk', 'id', 'name', 'status', 'platform', 'site',
            'resource_account', 'tenant', 'sync_status', 'last_synced',
            'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'status', 'platform', 'site', 'resource_account',
        )
