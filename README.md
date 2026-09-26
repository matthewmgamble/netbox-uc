# NetBox UC

A [NetBox](https://github.com/netbox-community/netbox) plugin for Unified Communications inventory, relationship, and lifecycle management.

## Features

- **Phone Numbers** — E.164-validated DID/toll-free/extension tracking with carrier, SIP trunk, and platform associations
- **Number Ranges** — Block allocation with utilization metrics
- **Resource Accounts** — Microsoft Teams resource accounts with sync metadata
- **Auto Attendants & Call Queues** — Service inventory with phone number assignments
- **User Accounts** — UC user profiles linked to platforms and tenants
- **Voice Endpoints** — Desk phones, softphones, and conference devices tied to NetBox devices/interfaces
- **Voice Locations & Emergency Addresses** — E911/E933 location management with lat/long coordinates and validation status
- **SIP Trunks & Endpoints** — Trunk configuration with carrier endpoint failover (FQDN/IP, port, priority)
- **Session Border Controllers** — SBC inventory linked to devices and SIP trunks
- **Carriers & UC Platforms** — Provider and platform registry
- **Microsoft Teams Sync** — Automated synchronization of resource accounts, auto attendants, call queues, and phone numbers via Microsoft Graph API
- **Reconciliation Engine** — Drift detection with missing → stale → archived lifecycle promotion
- **Full REST API** — Complete CRUD API for all models via NetBox's plugin API framework

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
| 4.0+           | 0.1.x          |

## Installation

1. Install the plugin (coming soon!):

```bash
pip install netbox-uc
```

Or for development:

```bash
cd /opt/netbox
git clone https://github.com/matthewmgamble/netbox-uc.git
pip install -e netbox-uc
```

2. Add the plugin to `configuration.py`:

```python
PLUGINS = ['netbox_uc']
```

3. Run migrations:

```bash
cd /opt/netbox/netbox
python manage.py migrate netbox_uc
```

4. Restart NetBox:

```bash
sudo systemctl restart netbox netbox-rq
```

## Microsoft Teams Sync

To sync data from Microsoft Teams, configure credentials in `configuration.py`:

```python
PLUGINS_CONFIG = {
    'netbox_uc': {
        'microsoft': {
            'tenant_id': '<your-entra-tenant-id>',
            'client_id': '<your-app-client-id>',
            'client_secret': '<your-app-client-secret>',
        }
    }
}
```

Then run the sync command:

```bash
cd /opt/netbox/netbox
python manage.py sync_teams
```

Options:

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview changes without writing |
| `--platform <name>` | Associate synced objects with a UC Platform |
| `--skip <type>` | Skip specific types: `resource-accounts`, `phone-numbers`, `auto-attendants`, `call-queues` |

## License

Apache License 2.0. See [LICENSE](LICENSE) for details.

