import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import PhoneNumber

__all__ = (
    'PhoneNumberTable',
)


class PhoneNumberTable(NetBoxTable):
    number = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    number_type = columns.ChoiceFieldColumn(verbose_name='Type')
    carrier = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    platform = tables.Column(linkify=True)
    sip_trunk = tables.Column(linkify=True, verbose_name='SIP Trunk')
    tenant = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = PhoneNumber
        fields = (
            'pk', 'id', 'number', 'extension', 'status', 'number_type',
            'carrier', 'site', 'platform', 'sip_trunk', 'tenant',
            'description', 'tags',
        )
        default_columns = ('pk', 'number', 'extension', 'status', 'number_type', 'carrier', 'sip_trunk', 'platform')
