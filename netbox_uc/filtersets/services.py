import django_filters
from django.db.models import Q
from dcim.models import Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import ServiceStatusChoices, SyncStatusChoices
from netbox_uc.models import AutoAttendant, CallQueue, UCPlatform

__all__ = (
    'AutoAttendantFilterSet',
    'CallQueueFilterSet',
)


class AutoAttendantFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=ServiceStatusChoices,
    )
    sync_status = django_filters.MultipleChoiceFilter(
        choices=SyncStatusChoices,
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
        model = AutoAttendant
        fields = ('id', 'name', 'status')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )


class CallQueueFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=ServiceStatusChoices,
    )
    sync_status = django_filters.MultipleChoiceFilter(
        choices=SyncStatusChoices,
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
        model = CallQueue
        fields = ('id', 'name', 'status')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )
