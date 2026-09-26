import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from netbox_uc.models import SessionBorderController, SIPTrunk, SIPTrunkEndpoint

__all__ = (
    'SIPTrunkTable',
    'SIPTrunkEndpointTable',
    'SessionBorderControllerTable',
)


class SIPTrunkTable(NetBoxTable):
    name = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn()
    direction = columns.ChoiceFieldColumn()
    carrier = tables.Column(linkify=True)
    platform = tables.Column(linkify=True)
    site = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = SIPTrunk
        fields = (
            'pk', 'id', 'name', 'status', 'direction', 'carrier', 'platform',
            'site', 'tenant', 'signaling_protocol', 'media_protocol',
            'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'status', 'direction', 'carrier', 'platform', 'site',
        )


class SIPTrunkEndpointTable(NetBoxTable):
    fqdn_or_ip = tables.Column(linkify=True, verbose_name='FQDN / IP')
    sip_trunk = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = SIPTrunkEndpoint
        fields = (
            'pk', 'id', 'fqdn_or_ip', 'port', 'protocol', 'priority',
            'sip_trunk', 'description', 'tags',
        )
        default_columns = ('pk', 'fqdn_or_ip', 'port', 'protocol', 'priority', 'sip_trunk')


class SessionBorderControllerTable(NetBoxTable):
    name = tables.Column(linkify=True)
    role = columns.ChoiceFieldColumn()
    status = columns.ChoiceFieldColumn()
    device = tables.Column(linkify=True)
    platform = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = SessionBorderController
        fields = (
            'pk', 'id', 'name', 'role', 'status', 'device', 'platform',
            'tenant', 'description', 'tags',
        )
        default_columns = (
            'pk', 'name', 'role', 'status', 'device', 'platform',
        )
