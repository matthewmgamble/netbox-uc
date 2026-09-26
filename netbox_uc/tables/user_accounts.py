import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import UserAccount

__all__ = (
    'UserAccountTable',
)


class UserAccountTable(NetBoxTable):
    display_name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    platform = tables.Column(linkify=True)
    phone_number = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = UserAccount
        fields = (
            'pk', 'id', 'display_name', 'user_principal_name', 'status',
            'platform', 'phone_number', 'extension', 'site', 'tenant',
            'description', 'tags',
        )
        default_columns = (
            'pk', 'display_name', 'user_principal_name', 'status',
            'platform', 'phone_number', 'site',
        )
