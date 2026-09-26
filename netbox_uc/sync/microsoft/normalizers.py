"""Normalize raw Microsoft Graph API data into internal format."""

import logging

logger = logging.getLogger('netbox_uc.sync.microsoft')


def normalize_resource_account(raw: dict) -> dict:
    """Normalize a Graph API user (resource account) to internal format."""
    return {
        'external_id': raw.get('id', ''),
        'display_name': raw.get('displayName', ''),
        'user_principal_name': raw.get('userPrincipalName', ''),
        'object_id': raw.get('id', ''),
    }


def normalize_auto_attendant(raw: dict) -> dict:
    """Normalize a Graph API auto attendant to internal format."""
    return {
        'external_id': raw.get('id', ''),
        'name': raw.get('name', raw.get('displayName', '')),
        'timezone': raw.get('timeZoneId', ''),
        'language': raw.get('languageId', ''),
    }


def normalize_call_queue(raw: dict) -> dict:
    """Normalize a Graph API call queue to internal format."""
    return {
        'external_id': raw.get('id', ''),
        'name': raw.get('name', raw.get('displayName', '')),
    }


def normalize_phone_number(raw: dict) -> dict:
    """Normalize a Graph API phone number to internal format."""
    number = raw.get('phoneNumber', raw.get('id', ''))
    # Ensure E.164 format
    if number and not number.startswith('+'):
        number = f'+{number}'

    return {
        'external_id': raw.get('id', number),
        'number': number,
        'number_type': _map_number_type(raw.get('phoneNumberType', '')),
        'status': _map_assignment_status(raw),
    }


def _map_number_type(graph_type: str) -> str:
    """Map Graph API phone number type to internal type."""
    mapping = {
        'user': 'did',
        'service': 'service',
        'tollFree': 'toll_free',
        'conference': 'service',
    }
    return mapping.get(graph_type, 'did')


def _map_assignment_status(raw: dict) -> str:
    """Determine phone number status from Graph API data."""
    if raw.get('assignedTo'):
        return 'assigned'
    if raw.get('assignmentStatus') == 'assigned':
        return 'assigned'
    return 'available'
