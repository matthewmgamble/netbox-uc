from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import NumberRangeStatusChoices
from netbox_uc.models import Carrier, NumberRange


class NumberRangeForm(NetBoxModelForm):
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
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'status', 'tags', name=_('Number Range')),
        FieldSet('start_number', 'end_number', name=_('Range')),
        FieldSet('carrier', name=_('Provider')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = NumberRange
        fields = (
            'name', 'start_number', 'end_number', 'carrier', 'status',
            'site', 'tenant', 'description', 'comments', 'tags',
        )


class NumberRangeFilterForm(NetBoxModelFilterSetForm):
    model = NumberRange
    status = forms.MultipleChoiceField(
        choices=NumberRangeStatusChoices,
        required=False,
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
    tenant_id = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_('Tenant'),
    )


class NumberRangeImportForm(NetBoxModelImportForm):
    carrier = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = NumberRange
        fields = (
            'name', 'start_number', 'end_number', 'carrier', 'status',
            'site', 'tenant', 'description',
        )


class NumberRangeBulkEditForm(NetBoxModelBulkEditForm):
    model = NumberRange
    status = forms.ChoiceField(
        choices=NumberRangeStatusChoices,
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
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('carrier', 'site', 'tenant', 'description')
