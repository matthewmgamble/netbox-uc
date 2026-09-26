from django import forms
from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField, SlugField
from utilities.forms.rendering import FieldSet
from netbox_uc.models import Carrier


class CarrierForm(NetBoxModelForm):
    slug = SlugField()
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'slug', 'description', 'tags', name=_('Carrier')),
        FieldSet('account_number', 'support_contact', 'portal_url', name=_('Details')),
        FieldSet('tenant', name=_('Tenancy')),
    )

    class Meta:
        model = Carrier
        fields = (
            'name', 'slug', 'account_number', 'support_contact', 'portal_url',
            'tenant', 'description', 'comments', 'tags',
        )


class CarrierFilterForm(NetBoxModelFilterSetForm):
    model = Carrier
    tenant_id = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_('Tenant'),
    )


class CarrierImportForm(NetBoxModelImportForm):
    tenant = forms.CharField(
        required=False,
    )

    class Meta:
        model = Carrier
        fields = (
            'name', 'slug', 'account_number', 'support_contact', 'portal_url',
            'tenant', 'description',
        )


class CarrierBulkEditForm(NetBoxModelBulkEditForm):
    model = Carrier
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('tenant', 'description')
