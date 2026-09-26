from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Device, Interface, Manufacturer, Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import VoiceEndpointStatusChoices, VoiceEndpointTypeChoices
from netbox_uc.models import PhoneNumber, ResourceAccount, UCPlatform, UserAccount, VoiceEndpoint


class VoiceEndpointForm(NetBoxModelForm):
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
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        query_params={
            'site_id': '$site',
        },
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        required=False,
        query_params={
            'device_id': '$device',
        },
    )
    phone_number = DynamicModelChoiceField(
        queryset=PhoneNumber.objects.all(),
        required=False,
    )
    user_account = DynamicModelChoiceField(
        queryset=UserAccount.objects.all(),
        required=False,
    )
    resource_account = DynamicModelChoiceField(
        queryset=ResourceAccount.objects.all(),
        required=False,
    )
    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'endpoint_type', 'status', 'tags', name=_('Voice Endpoint')),
        FieldSet('platform', 'site', 'tenant', name=_('Assignment')),
        FieldSet('device', 'interface', name=_('Physical Device')),
        FieldSet('phone_number', 'user_account', 'resource_account', name=_('UC Assignment')),
        FieldSet('manufacturer', 'model', 'serial_number', 'mac_address', 'firmware', name=_('Hardware')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = VoiceEndpoint
        fields = (
            'name', 'endpoint_type', 'platform', 'site', 'tenant',
            'device', 'interface', 'phone_number', 'user_account',
            'resource_account', 'manufacturer', 'model', 'serial_number',
            'mac_address', 'firmware', 'status', 'external_id',
            'description', 'comments', 'tags',
        )


class VoiceEndpointFilterForm(NetBoxModelFilterSetForm):
    model = VoiceEndpoint
    status = forms.MultipleChoiceField(
        choices=VoiceEndpointStatusChoices,
        required=False,
    )
    endpoint_type = forms.MultipleChoiceField(
        choices=VoiceEndpointTypeChoices,
        required=False,
        label=_('Type'),
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
    manufacturer_id = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_('Manufacturer'),
    )


class VoiceEndpointImportForm(NetBoxModelImportForm):
    platform = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = VoiceEndpoint
        fields = (
            'name', 'endpoint_type', 'platform', 'site', 'tenant',
            'model', 'serial_number', 'mac_address', 'firmware',
            'status', 'external_id', 'description',
        )


class VoiceEndpointBulkEditForm(NetBoxModelBulkEditForm):
    model = VoiceEndpoint
    status = forms.ChoiceField(
        choices=VoiceEndpointStatusChoices,
        required=False,
    )
    endpoint_type = forms.ChoiceField(
        choices=VoiceEndpointTypeChoices,
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
    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = (
        'platform', 'site', 'tenant', 'device', 'interface',
        'phone_number', 'user_account', 'resource_account',
        'manufacturer', 'description',
    )
