import logging
import time

from django.core.management.base import BaseCommand, CommandError

from netbox.plugins import get_plugin_config
from netbox_uc.models import UCPlatform
from netbox_uc.sync.microsoft import (
    TeamsAutoAttendantAdapter,
    TeamsCallQueueAdapter,
    TeamsPhoneNumberAdapter,
    TeamsResourceAccountAdapter,
)

logger = logging.getLogger('netbox_uc.sync')


class Command(BaseCommand):
    help = 'Synchronize Microsoft Teams Calling data into NetBox UC'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be synced without making changes',
        )
        parser.add_argument(
            '--tenant-id',
            type=str,
            help='Microsoft Entra tenant ID (overrides plugin config)',
        )
        parser.add_argument(
            '--client-id',
            type=str,
            help='Microsoft app client ID (overrides plugin config)',
        )
        parser.add_argument(
            '--platform',
            type=str,
            help='Name of the UCPlatform to associate synced objects with',
        )
        parser.add_argument(
            '--skip',
            nargs='+',
            choices=['resource-accounts', 'phone-numbers', 'auto-attendants', 'call-queues'],
            default=[],
            help='Skip specific object types during sync',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        skip = set(options['skip'])

        # Resolve Microsoft credentials
        ms_config = get_plugin_config('netbox_uc', 'microsoft') or {}
        tenant_id = options['tenant_id'] or ms_config.get('tenant_id', '')
        client_id = options['client_id'] or ms_config.get('client_id', '')
        client_secret = ms_config.get('client_secret', '')

        if not all([tenant_id, client_id, client_secret]):
            raise CommandError(
                'Microsoft credentials required. Set tenant_id, client_id, and '
                'client_secret in the plugin config (PLUGINS_CONFIG). '
                'tenant_id and client_id may also be passed via '
                '--tenant-id and --client-id arguments.'
            )

        # Resolve platform
        platform = None
        platform_name = options['platform']
        if platform_name:
            try:
                platform = UCPlatform.objects.get(name=platform_name)
            except UCPlatform.DoesNotExist:
                raise CommandError(f'UC Platform "{platform_name}" not found.')

        if dry_run:
            self.stdout.write(self.style.WARNING('DRY RUN - no changes will be made'))

        start_time = time.time()

        # Run sync adapters
        adapters = []
        if 'resource-accounts' not in skip:
            adapters.append(('Resource Accounts', TeamsResourceAccountAdapter(
                tenant_id, client_id, client_secret, platform=platform,
            )))
        if 'phone-numbers' not in skip:
            adapters.append(('Phone Numbers', TeamsPhoneNumberAdapter(
                tenant_id, client_id, client_secret, platform=platform,
            )))
        if 'auto-attendants' not in skip:
            adapters.append(('Auto Attendants', TeamsAutoAttendantAdapter(
                tenant_id, client_id, client_secret, platform=platform,
            )))
        if 'call-queues' not in skip:
            adapters.append(('Call Queues', TeamsCallQueueAdapter(
                tenant_id, client_id, client_secret, platform=platform,
            )))

        total_created = 0
        total_updated = 0
        total_errors = 0

        for label, adapter in adapters:
            self.stdout.write(f'\nSyncing {label}...')
            try:
                result = adapter.sync(dry_run=dry_run)
                self.stdout.write(
                    f'  Created: {result.created}, '
                    f'Updated: {result.updated}, '
                    f'Unchanged: {result.unchanged}, '
                    f'Missing: {result.missing}'
                )
                if result.errors:
                    for error in result.errors:
                        self.stdout.write(self.style.ERROR(f'  Error: {error}'))

                total_created += result.created
                total_updated += result.updated
                total_errors += len(result.errors)
            except Exception:
                self.stdout.write(self.style.ERROR(
                    f'  Failed — check logs for details (enable DEBUG for full traceback)'
                ))
                logger.error("Sync failed for %s", label, exc_info=logger.isEnabledFor(logging.DEBUG))
                total_errors += 1

        elapsed = time.time() - start_time

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Sync complete in {elapsed:.1f}s: '
            f'{total_created} created, {total_updated} updated, '
            f'{total_errors} errors'
        ))
