from django import forms
from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelImportForm
from utilities.forms.fields import CommentField, SlugField
from utilities.forms.rendering import FieldSet
from netbox_uc.choices import UCPlatformStatusChoices
from netbox_uc.models import UCPlatform


class UCPlatformForm(NetBoxModelForm):
    slug = SlugField()
    comments = CommentField()

    fieldsets = (
        FieldSet('name', 'slug', 'status', 'description', 'tags', name=_('Platform')),
        FieldSet('platform_type', 'version', name=_('Details')),
    )

    class Meta:
        model = UCPlatform
        fields = (
            'name', 'slug', 'platform_type', 'version', 'status',
            'description', 'comments', 'tags',
        )


class UCPlatformFilterForm(NetBoxModelFilterSetForm):
    model = UCPlatform
    status = forms.MultipleChoiceField(
        choices=UCPlatformStatusChoices,
        required=False,
    )


class UCPlatformImportForm(NetBoxModelImportForm):
    class Meta:
        model = UCPlatform
        fields = (
            'name', 'slug', 'platform_type', 'version', 'status', 'description',
        )


class UCPlatformBulkEditForm(NetBoxModelBulkEditForm):
    model = UCPlatform
    status = forms.ChoiceField(
        choices=UCPlatformStatusChoices,
        required=False,
    )
    description = forms.CharField(
        max_length=200,
        required=False,
    )
    nullable_fields = ('description',)
