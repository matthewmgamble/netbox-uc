import django_filters
from django.db.models import Q
from dcim.models import Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import NumberTypeChoices, PhoneNumberStatusChoices
from netbox_uc.models import Carrier, PhoneNumber, SIPTrunk, UCPlatform

__all__ = (
    'PhoneNumberFilterSet',
)


class PhoneNumberFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=PhoneNumberStatusChoices,
    )
    number_type = django_filters.MultipleChoiceFilter(
        choices=NumberTypeChoices,
    )
    carrier_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Carrier.objects.all(),
        label='Carrier (ID)',
    )
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label='Site (ID)',
    )
    platform_id = django_filters.ModelMultipleChoiceFilter(
        queryset=UCPlatform.objects.all(),
        label='Platform (ID)',
    )
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant (ID)',
    )
    sip_trunk_id = django_filters.ModelMultipleChoiceFilter(
        queryset=SIPTrunk.objects.all(),
        label='SIP Trunk (ID)',
    )

    class Meta:
        model = PhoneNumber
        fields = ('id', 'number', 'extension', 'status', 'number_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(number__icontains=value) |
            Q(extension__icontains=value) |
            Q(description__icontains=value)
        )
