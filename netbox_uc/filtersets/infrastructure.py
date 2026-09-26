import django_filters
from django.db.models import Q
from dcim.models import Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import (
    SBCRoleChoices, ServiceStatusChoices, SIPTrunkDirectionChoices, SIPTrunkStatusChoices,
)
from netbox_uc.models import Carrier, SessionBorderController, SIPTrunk, SIPTrunkEndpoint, UCPlatform

__all__ = (
    'SIPTrunkFilterSet',
    'SIPTrunkEndpointFilterSet',
    'SessionBorderControllerFilterSet',
)


class SIPTrunkFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=SIPTrunkStatusChoices,
    )
    direction = django_filters.MultipleChoiceFilter(
        choices=SIPTrunkDirectionChoices,
    )
    carrier_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Carrier.objects.all(),
        label='Carrier (ID)',
    )
    platform_id = django_filters.ModelMultipleChoiceFilter(
        queryset=UCPlatform.objects.all(),
        label='Platform (ID)',
    )
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label='Site (ID)',
    )
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant (ID)',
    )

    class Meta:
        model = SIPTrunk
        fields = ('id', 'name', 'status', 'direction')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )


class SIPTrunkEndpointFilterSet(NetBoxModelFilterSet):
    sip_trunk_id = django_filters.ModelMultipleChoiceFilter(
        queryset=SIPTrunk.objects.all(),
        label='SIP Trunk (ID)',
    )

    class Meta:
        model = SIPTrunkEndpoint
        fields = ('id', 'fqdn_or_ip', 'port', 'priority')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(fqdn_or_ip__icontains=value) |
            Q(description__icontains=value)
        )


class SessionBorderControllerFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=ServiceStatusChoices,
    )
    role = django_filters.MultipleChoiceFilter(
        choices=SBCRoleChoices,
    )
    platform_id = django_filters.ModelMultipleChoiceFilter(
        queryset=UCPlatform.objects.all(),
        label='Platform (ID)',
    )
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant (ID)',
    )

    class Meta:
        model = SessionBorderController
        fields = ('id', 'name', 'status', 'role')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )
