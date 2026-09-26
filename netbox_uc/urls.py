from django.urls import include, path
from utilities.urls import get_model_urls
from netbox_uc import models, views

urlpatterns = [
    # Carriers
    path('carriers/', views.CarrierListView.as_view(), name='carrier_list'),
    path('carriers/add/', views.CarrierEditView.as_view(), name='carrier_add'),
    path('carriers/import/', views.CarrierBulkImportView.as_view(), name='carrier_import'),
    path('carriers/edit/', views.CarrierBulkEditView.as_view(), name='carrier_bulk_edit'),
    path('carriers/delete/', views.CarrierBulkDeleteView.as_view(), name='carrier_bulk_delete'),
    path('carriers/<int:pk>/', include(get_model_urls('netbox_uc', 'carrier'))),

    # UC Platforms
    path('platforms/', views.UCPlatformListView.as_view(), name='ucplatform_list'),
    path('platforms/add/', views.UCPlatformEditView.as_view(), name='ucplatform_add'),
    path('platforms/import/', views.UCPlatformBulkImportView.as_view(), name='ucplatform_import'),
    path('platforms/edit/', views.UCPlatformBulkEditView.as_view(), name='ucplatform_bulk_edit'),
    path('platforms/delete/', views.UCPlatformBulkDeleteView.as_view(), name='ucplatform_bulk_delete'),
    path('platforms/<int:pk>/', include(get_model_urls('netbox_uc', 'ucplatform'))),

    # Phone Numbers
    path('phone-numbers/', views.PhoneNumberListView.as_view(), name='phonenumber_list'),
    path('phone-numbers/add/', views.PhoneNumberEditView.as_view(), name='phonenumber_add'),
    path('phone-numbers/import/', views.PhoneNumberBulkImportView.as_view(), name='phonenumber_import'),
    path('phone-numbers/edit/', views.PhoneNumberBulkEditView.as_view(), name='phonenumber_bulk_edit'),
    path('phone-numbers/delete/', views.PhoneNumberBulkDeleteView.as_view(), name='phonenumber_bulk_delete'),
    path('phone-numbers/<int:pk>/', include(get_model_urls('netbox_uc', 'phonenumber'))),

    # Number Ranges
    path('number-ranges/', views.NumberRangeListView.as_view(), name='numberrange_list'),
    path('number-ranges/add/', views.NumberRangeEditView.as_view(), name='numberrange_add'),
    path('number-ranges/import/', views.NumberRangeBulkImportView.as_view(), name='numberrange_import'),
    path('number-ranges/edit/', views.NumberRangeBulkEditView.as_view(), name='numberrange_bulk_edit'),
    path('number-ranges/delete/', views.NumberRangeBulkDeleteView.as_view(), name='numberrange_bulk_delete'),
    path('number-ranges/<int:pk>/', include(get_model_urls('netbox_uc', 'numberrange'))),

    # Resource Accounts
    path('resource-accounts/', views.ResourceAccountListView.as_view(), name='resourceaccount_list'),
    path('resource-accounts/add/', views.ResourceAccountEditView.as_view(), name='resourceaccount_add'),
    path('resource-accounts/import/', views.ResourceAccountBulkImportView.as_view(), name='resourceaccount_import'),
    path('resource-accounts/edit/', views.ResourceAccountBulkEditView.as_view(), name='resourceaccount_bulk_edit'),
    path('resource-accounts/delete/', views.ResourceAccountBulkDeleteView.as_view(), name='resourceaccount_bulk_delete'),
    path('resource-accounts/<int:pk>/', include(get_model_urls('netbox_uc', 'resourceaccount'))),

    # Auto Attendants
    path('auto-attendants/', views.AutoAttendantListView.as_view(), name='autoattendant_list'),
    path('auto-attendants/add/', views.AutoAttendantEditView.as_view(), name='autoattendant_add'),
    path('auto-attendants/import/', views.AutoAttendantBulkImportView.as_view(), name='autoattendant_import'),
    path('auto-attendants/edit/', views.AutoAttendantBulkEditView.as_view(), name='autoattendant_bulk_edit'),
    path('auto-attendants/delete/', views.AutoAttendantBulkDeleteView.as_view(), name='autoattendant_bulk_delete'),
    path('auto-attendants/<int:pk>/', include(get_model_urls('netbox_uc', 'autoattendant'))),

    # Call Queues
    path('call-queues/', views.CallQueueListView.as_view(), name='callqueue_list'),
    path('call-queues/add/', views.CallQueueEditView.as_view(), name='callqueue_add'),
    path('call-queues/import/', views.CallQueueBulkImportView.as_view(), name='callqueue_import'),
    path('call-queues/edit/', views.CallQueueBulkEditView.as_view(), name='callqueue_bulk_edit'),
    path('call-queues/delete/', views.CallQueueBulkDeleteView.as_view(), name='callqueue_bulk_delete'),
    path('call-queues/<int:pk>/', include(get_model_urls('netbox_uc', 'callqueue'))),

    # Voice Locations
    path('voice-locations/', views.VoiceLocationListView.as_view(), name='voicelocation_list'),
    path('voice-locations/add/', views.VoiceLocationEditView.as_view(), name='voicelocation_add'),
    path('voice-locations/import/', views.VoiceLocationBulkImportView.as_view(), name='voicelocation_import'),
    path('voice-locations/edit/', views.VoiceLocationBulkEditView.as_view(), name='voicelocation_bulk_edit'),
    path('voice-locations/delete/', views.VoiceLocationBulkDeleteView.as_view(), name='voicelocation_bulk_delete'),
    path('voice-locations/<int:pk>/', include(get_model_urls('netbox_uc', 'voicelocation'))),

    # Emergency Addresses
    path('emergency-addresses/', views.EmergencyAddressListView.as_view(), name='emergencyaddress_list'),
    path('emergency-addresses/add/', views.EmergencyAddressEditView.as_view(), name='emergencyaddress_add'),
    path('emergency-addresses/import/', views.EmergencyAddressBulkImportView.as_view(), name='emergencyaddress_import'),
    path('emergency-addresses/edit/', views.EmergencyAddressBulkEditView.as_view(), name='emergencyaddress_bulk_edit'),
    path('emergency-addresses/delete/', views.EmergencyAddressBulkDeleteView.as_view(), name='emergencyaddress_bulk_delete'),
    path('emergency-addresses/<int:pk>/', include(get_model_urls('netbox_uc', 'emergencyaddress'))),

    # Voice Endpoints
    path('voice-endpoints/', views.VoiceEndpointListView.as_view(), name='voiceendpoint_list'),
    path('voice-endpoints/add/', views.VoiceEndpointEditView.as_view(), name='voiceendpoint_add'),
    path('voice-endpoints/import/', views.VoiceEndpointBulkImportView.as_view(), name='voiceendpoint_import'),
    path('voice-endpoints/edit/', views.VoiceEndpointBulkEditView.as_view(), name='voiceendpoint_bulk_edit'),
    path('voice-endpoints/delete/', views.VoiceEndpointBulkDeleteView.as_view(), name='voiceendpoint_bulk_delete'),
    path('voice-endpoints/<int:pk>/', include(get_model_urls('netbox_uc', 'voiceendpoint'))),

    # User Accounts
    path('user-accounts/', views.UserAccountListView.as_view(), name='useraccount_list'),
    path('user-accounts/add/', views.UserAccountEditView.as_view(), name='useraccount_add'),
    path('user-accounts/import/', views.UserAccountBulkImportView.as_view(), name='useraccount_import'),
    path('user-accounts/edit/', views.UserAccountBulkEditView.as_view(), name='useraccount_bulk_edit'),
    path('user-accounts/delete/', views.UserAccountBulkDeleteView.as_view(), name='useraccount_bulk_delete'),
    path('user-accounts/<int:pk>/', include(get_model_urls('netbox_uc', 'useraccount'))),

    # SIP Trunks
    path('sip-trunks/', views.SIPTrunkListView.as_view(), name='siptrunk_list'),
    path('sip-trunks/add/', views.SIPTrunkEditView.as_view(), name='siptrunk_add'),
    path('sip-trunks/import/', views.SIPTrunkBulkImportView.as_view(), name='siptrunk_import'),
    path('sip-trunks/edit/', views.SIPTrunkBulkEditView.as_view(), name='siptrunk_bulk_edit'),
    path('sip-trunks/delete/', views.SIPTrunkBulkDeleteView.as_view(), name='siptrunk_bulk_delete'),
    path('sip-trunks/<int:pk>/', include(get_model_urls('netbox_uc', 'siptrunk'))),

    # SIP Trunk Endpoints
    path('sip-trunk-endpoints/', views.SIPTrunkEndpointListView.as_view(), name='siptrunkendpoint_list'),
    path('sip-trunk-endpoints/add/', views.SIPTrunkEndpointEditView.as_view(), name='siptrunkendpoint_add'),
    path('sip-trunk-endpoints/import/', views.SIPTrunkEndpointBulkImportView.as_view(), name='siptrunkendpoint_import'),
    path('sip-trunk-endpoints/edit/', views.SIPTrunkEndpointBulkEditView.as_view(), name='siptrunkendpoint_bulk_edit'),
    path('sip-trunk-endpoints/delete/', views.SIPTrunkEndpointBulkDeleteView.as_view(), name='siptrunkendpoint_bulk_delete'),
    path('sip-trunk-endpoints/<int:pk>/', include(get_model_urls('netbox_uc', 'siptrunkendpoint'))),

    # Session Border Controllers
    path('sbcs/', views.SessionBorderControllerListView.as_view(), name='sessionbordercontroller_list'),
    path('sbcs/add/', views.SessionBorderControllerEditView.as_view(), name='sessionbordercontroller_add'),
    path('sbcs/import/', views.SessionBorderControllerBulkImportView.as_view(), name='sessionbordercontroller_import'),
    path('sbcs/edit/', views.SessionBorderControllerBulkEditView.as_view(), name='sessionbordercontroller_bulk_edit'),
    path('sbcs/delete/', views.SessionBorderControllerBulkDeleteView.as_view(), name='sessionbordercontroller_bulk_delete'),
    path('sbcs/<int:pk>/', include(get_model_urls('netbox_uc', 'sessionbordercontroller'))),
]
