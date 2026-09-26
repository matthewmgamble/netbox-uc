from django import forms
from django.utils.translation import gettext_lazy as _
from dcim.models import Site
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import ServiceStatusChoices
from netbox_uc.models import AutoAttendant, CallQueue, ResourceAccount, UCPlatform


#
# Auto Attendant
#

class AutoAttendantForm(NetBoxModelForm):
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
    resource_account = DynamicModelChoiceField(
        queryset=ResourceAccount.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'status', 'tags', name=_('Auto Attendant')),
        FieldSet('platform', 'resource_account', name=_('Configuration')),
        FieldSet('timezone', 'language', name=_('Locale')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = AutoAttendant
        fields = (
            'name', 'platform', 'site', 'tenant', 'resource_account',
            'status', 'timezone', 'language', 'external_id',
            'description', 'comments', 'tags',
        )


class AutoAttendantFilterForm(NetBoxModelFilterSetForm):
    model = AutoAttendant
    status = forms.MultipleChoiceField(
        choices=ServiceStatusChoices,
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


class AutoAttendantImportForm(NetBoxModelImportForm):
    platform = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = AutoAttendant
        fields = (
            'name', 'platform', 'site', 'tenant', 'status',
            'timezone', 'language', 'external_id', 'description',
        )


class AutoAttendantBulkEditForm(NetBoxModelBulkEditForm):
    model = AutoAttendant
    status = forms.ChoiceField(
        choices=ServiceStatusChoices,
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
    nullable_fields = ('platform', 'site', 'tenant', 'resource_account', 'description')


#
# Call Queue
#

class CallQueueForm(NetBoxModelForm):
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
    resource_account = DynamicModelChoiceField(
        queryset=ResourceAccount.objects.all(),
        required=False,
    )
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'status', 'tags', name=_('Call Queue')),
        FieldSet('platform', 'resource_account', name=_('Configuration')),
        FieldSet('site', 'tenant', name=_('Assignment')),
        FieldSet('external_id', name=_('External References')),
        FieldSet('description', name=_('Details')),
    )

    class Meta:
        model = CallQueue
        fields = (
            'name', 'platform', 'site', 'tenant', 'resource_account',
            'status', 'external_id', 'description', 'comments', 'tags',
        )


class CallQueueFilterForm(NetBoxModelFilterSetForm):
    model = CallQueue
    status = forms.MultipleChoiceField(
        choices=ServiceStatusChoices,
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


class CallQueueImportForm(NetBoxModelImportForm):
    platform = forms.CharField(required=False)
    site = forms.CharField(required=False)
    tenant = forms.CharField(required=False)

    class Meta:
        model = CallQueue
        fields = (
            'name', 'platform', 'site', 'tenant', 'status',
            'external_id', 'description',
        )


class CallQueueBulkEditForm(NetBoxModelBulkEditForm):
    model = CallQueue
    status = forms.ChoiceField(
        choices=ServiceStatusChoices,
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
    nullable_fields = ('platform', 'site', 'tenant', 'resource_account', 'description')
