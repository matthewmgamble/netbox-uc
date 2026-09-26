import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import ResourceAccount

__all__ = (
    'ResourceAccountTable',
)


class ResourceAccountTable(NetBoxTable):
    display_name = tables.Column(linkify=True)
    resource_account_type = columns.ChoiceFieldColumn(verbose_name='Type')
    status = columns.ChoiceFieldColumn()
    platform = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    phone_number = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    sync_status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = ResourceAccount
        fields = (
            'pk', 'id', 'display_name', 'user_principal_name',
            'resource_account_type', 'status', 'platform', 'site',
            'phone_number', 'tenant', 'sync_status', 'last_synced',
            'description', 'tags',
        )
        default_columns = (
            'pk', 'display_name', 'user_principal_name',
            'resource_account_type', 'status', 'platform', 'site', 'phone_number',
        )
