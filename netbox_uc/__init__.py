from netbox.plugins import PluginConfig


class NetBoxUCConfig(PluginConfig):
    name = 'netbox_uc'
    verbose_name = 'NetBox Unified Communications'
    description = 'Unified Communications inventory, relationship, and lifecycle management for NetBox'
    version = '0.1.0'
    author = 'Matthew Gamble'
    author_email = ''
    base_url = 'netbox-uc'
    min_version = '4.0.0'
    default_settings = {
        'top_level_menu': True,
        'enforce_e164': True,
    }


config = NetBoxUCConfig
