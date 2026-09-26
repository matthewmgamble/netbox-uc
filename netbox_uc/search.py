from netbox.search import SearchIndex, register_search
from netbox_uc.models import (
    AutoAttendant, CallQueue, Carrier, EmergencyAddress, NumberRange,
    PhoneNumber, ResourceAccount, SessionBorderController, SIPTrunk,
    SIPTrunkEndpoint, UCPlatform, UserAccount, VoiceEndpoint, VoiceLocation,
)


@register_search
class PhoneNumberIndex(SearchIndex):
    model = PhoneNumber
    fields = (
        ('number', 50),
        ('extension', 100),
        ('description', 500),
    )
    display_attrs = ('status', 'number_type', 'carrier', 'site')


@register_search
class CarrierIndex(SearchIndex):
    model = Carrier
    fields = (
        ('name', 100),
        ('account_number', 200),
        ('description', 500),
    )
    display_attrs = ('description',)


@register_search
class UCPlatformIndex(SearchIndex):
    model = UCPlatform
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('platform_type', 'status')


@register_search
class ResourceAccountIndex(SearchIndex):
    model = ResourceAccount
    fields = (
        ('display_name', 100),
        ('user_principal_name', 100),
        ('description', 500),
    )
    display_attrs = ('resource_account_type', 'status', 'platform', 'site')


@register_search
class AutoAttendantIndex(SearchIndex):
    model = AutoAttendant
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('status', 'platform', 'site')


@register_search
class CallQueueIndex(SearchIndex):
    model = CallQueue
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('status', 'platform', 'site')


@register_search
class VoiceEndpointIndex(SearchIndex):
    model = VoiceEndpoint
    fields = (
        ('name', 100),
        ('serial_number', 200),
        ('mac_address', 200),
        ('description', 500),
    )
    display_attrs = ('endpoint_type', 'status', 'platform', 'site')


@register_search
class VoiceLocationIndex(SearchIndex):
    model = VoiceLocation
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('site', 'platform')


@register_search
class EmergencyAddressIndex(SearchIndex):
    model = EmergencyAddress
    fields = (
        ('name', 100),
        ('street', 200),
        ('city', 200),
        ('postal_code', 200),
        ('description', 500),
    )
    display_attrs = ('city', 'province_state', 'validated')


@register_search
class UserAccountIndex(SearchIndex):
    model = UserAccount
    fields = (
        ('display_name', 100),
        ('user_principal_name', 100),
        ('description', 500),
    )
    display_attrs = ('status', 'platform', 'site')


@register_search
class NumberRangeIndex(SearchIndex):
    model = NumberRange
    fields = (
        ('name', 100),
        ('start_number', 200),
        ('end_number', 200),
        ('description', 500),
    )
    display_attrs = ('status', 'carrier', 'site')


@register_search
class SIPTrunkEndpointIndex(SearchIndex):
    model = SIPTrunkEndpoint
    fields = (
        ('fqdn_or_ip', 100),
        ('description', 500),
    )
    display_attrs = ('port', 'priority', 'sip_trunk')


@register_search
class SIPTrunkIndex(SearchIndex):
    model = SIPTrunk
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('status', 'direction', 'carrier', 'platform')


@register_search
class SessionBorderControllerIndex(SearchIndex):
    model = SessionBorderController
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('role', 'status', 'platform')
