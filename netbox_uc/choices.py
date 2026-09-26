from utilities.choices import ChoiceSet


class PhoneNumberStatusChoices(ChoiceSet):
    key = 'PhoneNumber.status'

    STATUS_AVAILABLE = 'available'
    STATUS_RESERVED = 'reserved'
    STATUS_ASSIGNED = 'assigned'
    STATUS_PORTING_IN = 'porting_in'
    STATUS_PORTING_OUT = 'porting_out'
    STATUS_DISCONNECTED = 'disconnected'
    STATUS_QUARANTINED = 'quarantined'
    STATUS_UNKNOWN = 'unknown'

    CHOICES = [
        (STATUS_AVAILABLE, 'Available', 'green'),
        (STATUS_RESERVED, 'Reserved', 'cyan'),
        (STATUS_ASSIGNED, 'Assigned', 'blue'),
        (STATUS_PORTING_IN, 'Porting In', 'orange'),
        (STATUS_PORTING_OUT, 'Porting Out', 'amber'),
        (STATUS_DISCONNECTED, 'Disconnected', 'red'),
        (STATUS_QUARANTINED, 'Quarantined', 'purple'),
        (STATUS_UNKNOWN, 'Unknown', 'gray'),
    ]


class NumberTypeChoices(ChoiceSet):
    key = 'PhoneNumber.number_type'

    TYPE_DID = 'did'
    TYPE_TOLL_FREE = 'toll_free'
    TYPE_MAIN = 'main'
    TYPE_EMERGENCY_CALLBACK = 'emergency_callback'
    TYPE_SHARED_CALLING = 'shared_calling'
    TYPE_FAX = 'fax'
    TYPE_ANALOG = 'analog'
    TYPE_SERVICE = 'service'
    TYPE_TEMPORARY = 'temporary'

    CHOICES = [
        (TYPE_DID, 'DID', 'blue'),
        (TYPE_TOLL_FREE, 'Toll Free', 'green'),
        (TYPE_MAIN, 'Main Number', 'indigo'),
        (TYPE_EMERGENCY_CALLBACK, 'Emergency Callback', 'red'),
        (TYPE_SHARED_CALLING, 'Shared Calling', 'teal'),
        (TYPE_FAX, 'Fax', 'gray'),
        (TYPE_ANALOG, 'Analog', 'amber'),
        (TYPE_SERVICE, 'Service Number', 'purple'),
        (TYPE_TEMPORARY, 'Temporary', 'orange'),
    ]


class NumberRangeStatusChoices(ChoiceSet):
    key = 'NumberRange.status'

    STATUS_ACTIVE = 'active'
    STATUS_RESERVED = 'reserved'
    STATUS_DEPLETED = 'depleted'

    CHOICES = [
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_RESERVED, 'Reserved', 'cyan'),
        (STATUS_DEPLETED, 'Depleted', 'red'),
    ]


class UCPlatformStatusChoices(ChoiceSet):
    key = 'UCPlatform.status'

    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_MIGRATING = 'migrating'
    STATUS_DECOMMISSIONED = 'decommissioned'

    CHOICES = [
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_MIGRATING, 'Migrating', 'orange'),
        (STATUS_DECOMMISSIONED, 'Decommissioned', 'gray'),
    ]


class ResourceAccountTypeChoices(ChoiceSet):
    key = 'ResourceAccount.resource_account_type'

    TYPE_AUTO_ATTENDANT = 'auto_attendant'
    TYPE_CALL_QUEUE = 'call_queue'
    TYPE_SHARED_CALLING = 'shared_calling'

    CHOICES = [
        (TYPE_AUTO_ATTENDANT, 'Auto Attendant', 'blue'),
        (TYPE_CALL_QUEUE, 'Call Queue', 'green'),
        (TYPE_SHARED_CALLING, 'Shared Calling', 'teal'),
    ]


class ServiceStatusChoices(ChoiceSet):
    key = 'Service.status'

    STATUS_ACTIVE = 'active'
    STATUS_DISABLED = 'disabled'
    STATUS_PLANNED = 'planned'

    CHOICES = [
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_DISABLED, 'Disabled', 'red'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
    ]


class VoiceEndpointTypeChoices(ChoiceSet):
    key = 'VoiceEndpoint.endpoint_type'

    TYPE_DESK_PHONE = 'desk_phone'
    TYPE_CONFERENCE_PHONE = 'conference_phone'
    TYPE_COMMON_AREA = 'common_area'
    TYPE_SOFTPHONE = 'softphone'
    TYPE_ATA = 'ata'
    TYPE_SIP_DEVICE = 'sip_device'
    TYPE_VIRTUAL = 'virtual'

    CHOICES = [
        (TYPE_DESK_PHONE, 'Desk Phone', 'blue'),
        (TYPE_CONFERENCE_PHONE, 'Conference Phone', 'indigo'),
        (TYPE_COMMON_AREA, 'Common Area Phone', 'teal'),
        (TYPE_SOFTPHONE, 'Softphone', 'green'),
        (TYPE_ATA, 'Analog Telephone Adapter', 'amber'),
        (TYPE_SIP_DEVICE, 'SIP Device', 'purple'),
        (TYPE_VIRTUAL, 'Virtual', 'gray'),
    ]


class VoiceEndpointStatusChoices(ChoiceSet):
    key = 'VoiceEndpoint.status'

    STATUS_ACTIVE = 'active'
    STATUS_OFFLINE = 'offline'
    STATUS_RMA = 'rma'
    STATUS_DECOMMISSIONED = 'decommissioned'

    CHOICES = [
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_OFFLINE, 'Offline', 'orange'),
        (STATUS_RMA, 'RMA', 'red'),
        (STATUS_DECOMMISSIONED, 'Decommissioned', 'gray'),
    ]


class SIPTrunkStatusChoices(ChoiceSet):
    key = 'SIPTrunk.status'

    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_DISABLED = 'disabled'
    STATUS_DECOMMISSIONED = 'decommissioned'

    CHOICES = [
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_DISABLED, 'Disabled', 'red'),
        (STATUS_DECOMMISSIONED, 'Decommissioned', 'gray'),
    ]


class SIPTrunkDirectionChoices(ChoiceSet):
    key = 'SIPTrunk.direction'

    DIRECTION_INBOUND = 'inbound'
    DIRECTION_OUTBOUND = 'outbound'
    DIRECTION_BIDIRECTIONAL = 'bidirectional'

    CHOICES = [
        (DIRECTION_INBOUND, 'Inbound', 'blue'),
        (DIRECTION_OUTBOUND, 'Outbound', 'green'),
        (DIRECTION_BIDIRECTIONAL, 'Bidirectional', 'purple'),
    ]


class SBCRoleChoices(ChoiceSet):
    key = 'SessionBorderController.role'

    ROLE_DIRECT_ROUTING = 'direct_routing'
    ROLE_CARRIER_EDGE = 'carrier_edge'
    ROLE_CONTACT_CENTRE = 'contact_centre'
    ROLE_LEGACY_INTEROP = 'legacy_interop'

    CHOICES = [
        (ROLE_DIRECT_ROUTING, 'Teams Direct Routing', 'blue'),
        (ROLE_CARRIER_EDGE, 'Carrier Edge', 'green'),
        (ROLE_CONTACT_CENTRE, 'Contact Centre', 'purple'),
        (ROLE_LEGACY_INTEROP, 'Legacy Interop', 'amber'),
    ]


class SyncStatusChoices(ChoiceSet):
    key = 'SyncStatus'

    STATUS_HEALTHY = 'healthy'
    STATUS_MISSING = 'missing'
    STATUS_STALE = 'stale'
    STATUS_ARCHIVED = 'archived'
    STATUS_CONFLICT = 'conflict'

    CHOICES = [
        (STATUS_HEALTHY, 'Healthy', 'green'),
        (STATUS_MISSING, 'Missing', 'orange'),
        (STATUS_STALE, 'Stale', 'amber'),
        (STATUS_ARCHIVED, 'Archived', 'gray'),
        (STATUS_CONFLICT, 'Conflict', 'red'),
    ]


class UserAccountStatusChoices(ChoiceSet):
    key = 'UserAccount.status'

    STATUS_ACTIVE = 'active'
    STATUS_DISABLED = 'disabled'
    STATUS_SUSPENDED = 'suspended'

    CHOICES = [
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_DISABLED, 'Disabled', 'red'),
        (STATUS_SUSPENDED, 'Suspended', 'orange'),
    ]
