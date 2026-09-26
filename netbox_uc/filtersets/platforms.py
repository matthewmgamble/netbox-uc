import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from netbox_uc.choices import UCPlatformStatusChoices
from netbox_uc.models import UCPlatform

__all__ = (
    'UCPlatformFilterSet',
)


class UCPlatformFilterSet(NetBoxModelFilterSet):
    status = django_filters.MultipleChoiceFilter(
        choices=UCPlatformStatusChoices,
    )

    class Meta:
        model = UCPlatform
        fields = ('id', 'name', 'slug', 'status', 'platform_type')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(platform_type__icontains=value) |
            Q(description__icontains=value)
        )
