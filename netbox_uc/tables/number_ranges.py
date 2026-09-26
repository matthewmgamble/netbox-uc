import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import NumberRange

__all__ = (
    'NumberRangeTable',
)


class NumberRangeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    carrier = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = NumberRange
        fields = (
            'pk', 'id', 'name', 'start_number', 'end_number', 'carrier',
            'status', 'site', 'tenant', 'description', 'tags',
        )
        default_columns = ('pk', 'name', 'start_number', 'end_number', 'carrier', 'status', 'site')
