import django_filters
from django.db.models import Q
from dcim.models import Site
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from netbox_uc.choices import ResourceAccountTypeChoices, ServiceStatusChoices, SyncStatusChoices
from netbox_uc.models import ResourceAccount, UCPlatform

__all__ = (
    'ResourceAccountFilterSet',
)


class ResourceAccountFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=ServiceStatusChoices,
    )
    resource_account_type = django_filters.MultipleChoiceFilter(
        choices=ResourceAccountTypeChoices,
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
        model = ResourceAccount
        fields = ('id', 'display_name', 'user_principal_name', 'resource_account_type', 'status')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(display_name__icontains=value) |
            Q(user_principal_name__icontains=value) |
            Q(description__icontains=value)
        )
