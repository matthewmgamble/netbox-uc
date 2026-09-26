from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Device, Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import SBCRoleChoices, ServiceStatusChoices, SIPTrunkDirectionChoices, SIPTrunkStatusChoices
from netbox_uc.models import Carrier, SessionBorderController, SIPTrunk, SIPTrunkEndpoint, UCPlatform


#
# SIP Trunk
#

class SIPTrunkForm(NetBoxModelForm):
    carrier = DynamicModelChoiceField(
        queryset=Carrier.objects.all(),
        required=False,
    )
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'status', 'direction', 'tags', name=_('SIP Trunk')),
        FieldSet('carrier', 'platform', name=_('Provider')),
        FieldSet('signaling_protocol', 'media_protocol', name=_('Protocols')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = SIPTrunk
        fields = (
            'name', 'carrier', 'platform', 'site', 'tenant', 'status',
            'direction', 'signaling_protocol', 'media_protocol',
            'external_id', 'description', 'comments', 'tags',
        )


class SIPTrunkFilterForm(NetBoxModelFilterSetForm):
    model = SIPTrunk
    status = forms.MultipleChoiceField(
        choices=SIPTrunkStatusChoices,
        required=False,
    )
    direction = forms.MultipleChoiceField(
        choices=SIPTrunkDirectionChoices,
        required=False,
    )
    carrier_id = DynamicModelChoiceField(
        queryset=Carrier.objects.all(),
        required=False,
        label=_('Carrier'),
    )
    platform_id = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
        label=_('Platform'),
    )
    site_id = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site'),
    )
    tenant_id = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_('Tenant'),
    )


class SIPTrunkImportForm(NetBoxModelImportForm):
    carrier = forms.CharField(required=False)
    platform = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = SIPTrunk
        fields = (
            'name', 'carrier', 'platform', 'site', 'tenant', 'status',
            'direction', 'signaling_protocol', 'media_protocol',
            'external_id', 'description',
        )


class SIPTrunkBulkEditForm(NetBoxModelBulkEditForm):
    model = SIPTrunk
    status = forms.ChoiceField(
        choices=SIPTrunkStatusChoices,
        required=False,
    )
    direction = forms.ChoiceField(
        choices=SIPTrunkDirectionChoices,
        required=False,
    )
    carrier = DynamicModelChoiceField(
        queryset=Carrier.objects.all(),
        required=False,
    )
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('carrier', 'platform', 'site', 'tenant', 'description')


#
# SIP Trunk Endpoint
#

class SIPTrunkEndpointForm(NetBoxModelForm):
    sip_trunk = DynamicModelChoiceField(
        queryset=SIPTrunk.objects.all(),
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('sip_trunk', 'fqdn_or_ip', 'port', 'protocol', 'priority', 'tags', name=_('SIP Trunk Endpoint')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = SIPTrunkEndpoint
        fields = (
            'sip_trunk', 'fqdn_or_ip', 'port', 'protocol', 'priority',
            'description', 'tags',
        )


class SIPTrunkEndpointFilterForm(NetBoxModelFilterSetForm):
    model = SIPTrunkEndpoint
    sip_trunk_id = DynamicModelChoiceField(
        queryset=SIPTrunk.objects.all(),
        required=False,
        label=_('SIP Trunk'),
    )


class SIPTrunkEndpointImportForm(NetBoxModelImportForm):
    sip_trunk = forms.CharField()

    class Meta:
        model = SIPTrunkEndpoint
        fields = (
            'sip_trunk', 'fqdn_or_ip', 'port', 'protocol', 'priority',
            'description',
        )


class SIPTrunkEndpointBulkEditForm(NetBoxModelBulkEditForm):
    model = SIPTrunkEndpoint
    port = forms.IntegerField(
        required=False,
    )
    protocol = forms.CharField(
        max_length=20,
        required=False,
    )
    priority = forms.IntegerField(
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('protocol', 'description')


#
# Session Border Controller
#

class SessionBorderControllerForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    sip_trunks = DynamicModelMultipleChoiceField(
        queryset=SIPTrunk.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'role', 'status', 'tags', name=_('Session Border Controller')),
        FieldSet('device', 'platform', name=_('Infrastructure')),
        FieldSet('sip_trunks', name=_('SIP Trunks')),
        FieldSet('tenant', name=_('Tenancy')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = SessionBorderController
        fields = (
            'name', 'device', 'platform', 'tenant', 'role', 'status',
            'sip_trunks', 'external_id', 'description', 'comments', 'tags',
        )


class SessionBorderControllerFilterForm(NetBoxModelFilterSetForm):
    model = SessionBorderController
    status = forms.MultipleChoiceField(
        choices=ServiceStatusChoices,
        required=False,
    )
    role = forms.MultipleChoiceField(
        choices=SBCRoleChoices,
        required=False,
    )
    platform_id = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
        label=_('Platform'),
    )
    tenant_id = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_('Tenant'),
    )


class SessionBorderControllerImportForm(NetBoxModelImportForm):
    platform = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = SessionBorderController
        fields = (
            'name', 'platform', 'tenant', 'role', 'status',
            'external_id', 'description',
        )


class SessionBorderControllerBulkEditForm(NetBoxModelBulkEditForm):
    model = SessionBorderController
    status = forms.ChoiceField(
        choices=ServiceStatusChoices,
        required=False,
    )
    role = forms.ChoiceField(
        choices=SBCRoleChoices,
        required=False,
    )
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('device', 'platform', 'tenant', 'description')
