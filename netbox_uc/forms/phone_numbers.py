from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import NumberTypeChoices, PhoneNumberStatusChoices
from netbox_uc.models import Carrier, PhoneNumber, SIPTrunk, UCPlatform


class PhoneNumberForm(NetBoxModelForm):
    carrier = DynamicModelChoiceField(
        queryset=Carrier.objects.all(),
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
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    sip_trunk = DynamicModelChoiceField(
        queryset=SIPTrunk.objects.all(),
        required=False,
        label=_('SIP Trunk'),
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('number', 'extension', 'status', 'number_type', 'tags', name=_('Phone Number')),
        FieldSet('carrier', 'platform', 'sip_trunk', name=_('Provider')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = PhoneNumber
        fields = (
            'number', 'extension', 'status', 'number_type', 'carrier',
            'site', 'tenant', 'platform', 'sip_trunk', 'description', 'comments', 'tags',
        )


class PhoneNumberFilterForm(NetBoxModelFilterSetForm):
    model = PhoneNumber
    status = forms.MultipleChoiceField(
        choices=PhoneNumberStatusChoices,
        required=False,
    )
    number_type = forms.MultipleChoiceField(
        choices=NumberTypeChoices,
        required=False,
        label=_('Type'),
    )
    carrier_id = DynamicModelChoiceField(
        queryset=Carrier.objects.all(),
        required=False,
        label=_('Carrier'),
    )
    site_id = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site'),
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
    sip_trunk_id = DynamicModelChoiceField(
        queryset=SIPTrunk.objects.all(),
        required=False,
        label=_('SIP Trunk'),
    )


class PhoneNumberImportForm(NetBoxModelImportForm):
    carrier = forms.CharField(
        required=False,
    )
    site = forms.CharField(
        required=False,
    )
    platform = forms.CharField(
        required=False,
    )
    tenant = forms.CharField(
        required=False,
    )

    sip_trunk = forms.CharField(required=False)

    class Meta:
        model = PhoneNumber
        fields = (
            'number', 'extension', 'status', 'number_type', 'carrier',
            'site', 'tenant', 'platform', 'sip_trunk', 'description',
        )


class PhoneNumberBulkEditForm(NetBoxModelBulkEditForm):
    model = PhoneNumber
    status = forms.ChoiceField(
        choices=PhoneNumberStatusChoices,
        required=False,
    )
    number_type = forms.ChoiceField(
        choices=NumberTypeChoices,
        required=False,
    )
    carrier = DynamicModelChoiceField(
        queryset=Carrier.objects.all(),
        required=False,
    )
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
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
    sip_trunk = DynamicModelChoiceField(
        queryset=SIPTrunk.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('carrier', 'site', 'platform', 'tenant', 'sip_trunk', 'description', 'extension')
