from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import ResourceAccountTypeChoices, ServiceStatusChoices
from netbox_uc.models import PhoneNumber, ResourceAccount, UCPlatform


class ResourceAccountForm(NetBoxModelForm):
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
    phone_number = DynamicModelChoiceField(
        queryset=PhoneNumber.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('display_name', 'user_principal_name', 'resource_account_type', 'status', 'tags', name=_('Resource Account')),
        FieldSet('platform', 'phone_number', name=_('Configuration')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('object_id', 'external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = ResourceAccount
        fields = (
            'display_name', 'user_principal_name', 'object_id',
            'resource_account_type', 'platform', 'site', 'tenant',
            'phone_number', 'status', 'external_id',
            'description', 'comments', 'tags',
        )


class ResourceAccountFilterForm(NetBoxModelFilterSetForm):
    model = ResourceAccount
    status = forms.MultipleChoiceField(
        choices=ServiceStatusChoices,
        required=False,
    )
    resource_account_type = forms.MultipleChoiceField(
        choices=ResourceAccountTypeChoices,
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


class ResourceAccountImportForm(NetBoxModelImportForm):
    platform = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = ResourceAccount
        fields = (
            'display_name', 'user_principal_name', 'object_id',
            'resource_account_type', 'platform', 'site', 'tenant',
            'status', 'external_id', 'description',
        )


class ResourceAccountBulkEditForm(NetBoxModelBulkEditForm):
    model = ResourceAccount
    status = forms.ChoiceField(
        choices=ServiceStatusChoices,
        required=False,
    )
    resource_account_type = forms.ChoiceField(
        choices=ResourceAccountTypeChoices,
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
    nullable_fields = ('platform', 'site', 'tenant', 'phone_number', 'description')
