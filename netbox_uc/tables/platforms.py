import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import UCPlatform

__all__ = (
    'UCPlatformTable',
)


class UCPlatformTable(NetBoxTable):
    name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = UCPlatform
        fields = (
            'pk', 'id', 'name', 'slug', 'platform_type', 'version',
            'status', 'description', 'tags',
        )
        default_columns = ('pk', 'name', 'platform_type', 'version', 'status')
