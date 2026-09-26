from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import UserAccountStatusChoices
from netbox_uc.models import PhoneNumber, UCPlatform, UserAccount


class UserAccountForm(NetBoxModelForm):
    platform = DynamicModelChoiceField(
        queryset=UCPlatform.objects.all(),
        required=False,
    )
    phone_number = DynamicModelChoiceField(
        queryset=PhoneNumber.objects.all(),
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
        FieldSet('display_name', 'user_principal_name', 'status', 'tags', name=_('User Account')),
        FieldSet('platform', 'phone_number', 'extension', name=_('Configuration')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = UserAccount
        fields = (
            'display_name', 'user_principal_name', 'external_id',
            'platform', 'phone_number', 'extension', 'site', 'tenant',
            'status', 'description', 'comments', 'tags',
        )


class UserAccountFilterForm(NetBoxModelFilterSetForm):
    model = UserAccount
    status = forms.MultipleChoiceField(
        choices=UserAccountStatusChoices,
        required=False,
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


class UserAccountImportForm(NetBoxModelImportForm):
    platform = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = UserAccount
        fields = (
            'display_name', 'user_principal_name', 'external_id',
            'platform', 'extension', 'site', 'tenant', 'status', 'description',
        )


class UserAccountBulkEditForm(NetBoxModelBulkEditForm):
    model = UserAccount
    status = forms.ChoiceField(
        choices=UserAccountStatusChoices,
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
    nullable_fields = ('platform', 'phone_number', 'site', 'tenant', 'description', 'extension')
