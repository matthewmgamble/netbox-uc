import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import Carrier

__all__ = (
    'CarrierTable',
)


class CarrierTable(NetBoxTable):
    name = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Carrier
        fields = (
            'pk', 'id', 'name', 'slug', 'account_number', 'support_contact',
            'portal_url', 'tenant', 'description', 'tags',
        )
        default_columns = ('pk', 'name', 'account_number', 'tenant', 'description')
