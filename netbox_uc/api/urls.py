from netbox.api.routers import NetBoxRouter
from netbox_uc.api import views

router = NetBoxRouter()

router.register('carriers', views.CarrierViewSet)
router.register('platforms', views.UCPlatformViewSet)
router.register('phone-numbers', views.PhoneNumberViewSet)
router.register('number-ranges', views.NumberRangeViewSet)
router.register('resource-accounts', views.ResourceAccountViewSet)
router.register('auto-attendants', views.AutoAttendantViewSet)
router.register('call-queues', views.CallQueueViewSet)
router.register('voice-locations', views.VoiceLocationViewSet)
router.register('emergency-addresses', views.EmergencyAddressViewSet)
router.register('voice-endpoints', views.VoiceEndpointViewSet)
router.register('user-accounts', views.UserAccountViewSet)
router.register('sip-trunks', views.SIPTrunkViewSet)
router.register('sip-trunk-endpoints', views.SIPTrunkEndpointViewSet)
router.register('sbcs', views.SessionBorderControllerViewSet)

urlpatterns = router.urls
