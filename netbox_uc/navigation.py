from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

menu = PluginMenu(
    label='NetBox Unified Communications',
    icon_class='mdi mdi-phone',
    groups=(
        ('Inventory', (
            PluginMenuItem(
                link='plugins:netbox_uc:voiceendpoint_list',
                link_text='Voice Endpoints',
                permissions=['netbox_uc.view_voiceendpoint'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:voiceendpoint_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_voiceendpoint'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:resourceaccount_list',
                link_text='Resource Accounts',
                permissions=['netbox_uc.view_resourceaccount'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:resourceaccount_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_resourceaccount'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:useraccount_list',
                link_text='User Accounts',
                permissions=['netbox_uc.view_useraccount'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:useraccount_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_useraccount'],
                    ),
                ),
            ),
        )),
        ('Numbers', (
            PluginMenuItem(
                link='plugins:netbox_uc:phonenumber_list',
                link_text='Phone Numbers',
                permissions=['netbox_uc.view_phonenumber'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:phonenumber_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_phonenumber'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:numberrange_list',
                link_text='Number Ranges',
                permissions=['netbox_uc.view_numberrange'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:numberrange_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_numberrange'],
                    ),
                ),
            ),
        )),
        ('Services', (
            PluginMenuItem(
                link='plugins:netbox_uc:autoattendant_list',
                link_text='Auto Attendants',
                permissions=['netbox_uc.view_autoattendant'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:autoattendant_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_autoattendant'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:callqueue_list',
                link_text='Call Queues',
                permissions=['netbox_uc.view_callqueue'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:callqueue_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_callqueue'],
                    ),
                ),
            ),
        )),
        ('Locations', (
            PluginMenuItem(
                link='plugins:netbox_uc:voicelocation_list',
                link_text='Voice Locations',
                permissions=['netbox_uc.view_voicelocation'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:voicelocation_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_voicelocation'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:emergencyaddress_list',
                link_text='Emergency Addresses',
                permissions=['netbox_uc.view_emergencyaddress'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:emergencyaddress_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_emergencyaddress'],
                    ),
                ),
            ),
        )),
        ('Infrastructure', (
            PluginMenuItem(
                link='plugins:netbox_uc:siptrunk_list',
                link_text='SIP Trunks',
                permissions=['netbox_uc.view_siptrunk'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:siptrunk_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_siptrunk'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:siptrunkendpoint_list',
                link_text='SIP Trunk Endpoints',
                permissions=['netbox_uc.view_siptrunkendpoint'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:siptrunkendpoint_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_siptrunkendpoint'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:carrier_list',
                link_text='Carriers',
                permissions=['netbox_uc.view_carrier'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:carrier_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_carrier'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:ucplatform_list',
                link_text='UC Platforms',
                permissions=['netbox_uc.view_ucplatform'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:ucplatform_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_ucplatform'],
                    ),
                ),
            ),
            PluginMenuItem(
                link='plugins:netbox_uc:sessionbordercontroller_list',
                link_text='Session Border Controllers',
                permissions=['netbox_uc.view_sessionbordercontroller'],
                buttons=(
                    PluginMenuButton(
                        link='plugins:netbox_uc:sessionbordercontroller_add',
                        title='Add',
                        icon_class='mdi mdi-plus-thick',
                        permissions=['netbox_uc.add_sessionbordercontroller'],
                    ),
                ),
            ),
        )),
    ),
)
