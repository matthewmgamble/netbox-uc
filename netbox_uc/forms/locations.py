from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Location, Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.models import EmergencyAddress, PhoneNumber, ResourceAccount, UCPlatform, VoiceLocation


#
# Emergency Address
#

class EmergencyAddressForm(NetBoxModelForm):
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'tags', name=_('Emergency Address')),
        FieldSet('street', 'city', 'province_state', 'postal_code', 'country', name=_('Address')),
        FieldSet('latitude', 'longitude', name=_('Coordinates')),
        FieldSet('site', 'validated', name=_('Validation')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = EmergencyAddress
        fields = (
            'name', 'street', 'city', 'province_state', 'postal_code',
            'country', 'latitude', 'longitude', 'site', 'validated',
            'external_id', 'description', 'comments', 'tags',
        )


class EmergencyAddressFilterForm(NetBoxModelFilterSetForm):
    model = EmergencyAddress
    validated = forms.NullBooleanField(
        required=False,
    )
    site_id = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site'),
    )


class EmergencyAddressImportForm(NetBoxModelImportForm):
    site = forms.CharField(required=False)

    class Meta:
        model = EmergencyAddress
        fields = (
            'name', 'street', 'city', 'province_state', 'postal_code',
            'country', 'latitude', 'longitude', 'site', 'validated',
            'external_id', 'description',
        )


class EmergencyAddressBulkEditForm(NetBoxModelBulkEditForm):
    model = EmergencyAddress
    validated = forms.NullBooleanField(
        required=False,
    )
    latitude = forms.DecimalField(
        max_digits=9,
        decimal_places=6,
        required=False,
    )
    longitude = forms.DecimalField(
        max_digits=9,
        decimal_places=6,
        required=False,
    )
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('latitude', 'longitude', 'site', 'description')


#
# Voice Location
#

class VoiceLocationForm(NetBoxModelForm):
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
    )
    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        required=False,
        query_params={
            'site_id': '$site',
        },
    )
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    emergency_address = DynamicModelChoiceField(
        queryset=EmergencyAddress.objects.all(),
        required=False,
    )
    emergency_callback_number = DynamicModelChoiceField(
        queryset=PhoneNumber.objects.all(),
        required=False,
    )
    shared_calling_resource_account = DynamicModelChoiceField(
        queryset=ResourceAccount.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'tags', name=_('Voice Location')),
        FieldSet('site', 'location', 'platform', 'tenant', name=_('Assignment')),
        FieldSet('emergency_address', 'emergency_callback_number', name=_('Emergency Calling')),
        FieldSet('shared_calling_resource_account', name=_('Shared Calling')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = VoiceLocation
        fields = (
            'name', 'site', 'location', 'platform', 'tenant',
            'emergency_address', 'emergency_callback_number',
            'shared_calling_resource_account', 'external_id',
            'description', 'comments', 'tags',
        )


class VoiceLocationFilterForm(NetBoxModelFilterSetForm):
    model = VoiceLocation
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


class VoiceLocationImportForm(NetBoxModelImportForm):
    site = forms.CharField(required=False)
    platform = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = VoiceLocation
        fields = (
            'name', 'site', 'platform', 'tenant', 'external_id', 'description',
        )


class VoiceLocationBulkEditForm(NetBoxModelBulkEditForm):
    model = VoiceLocation
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
    nullable_fields = (
        'site', 'location', 'platform', 'tenant', 'emergency_address',
        'emergency_callback_number', 'shared_calling_resource_account', 'description',
    )
