from netbox.api.viewsets import NetBoxModelViewSet
from netbox_uc.api.serializers import UserAccountSerializer
from netbox_uc.filtersets import UserAccountFilterSet
from netbox_uc.models import UserAccount

__all__ = (
    'UserAccountViewSet',
)


class UserAccountViewSet(NetBoxModelViewSet):
    queryset = UserAccount.objects.prefetch_related('platform', 'phone_number', 'site', 'tenant', 'tags')
    serializer_class = UserAccountSerializer
    filterset_class = UserAccountFilterSet
