from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'EmergencyAddressListView',
    'EmergencyAddressView',
    'EmergencyAddressEditView',
    'EmergencyAddressDeleteView',
    'EmergencyAddressBulkImportView',
    'EmergencyAddressBulkEditView',
    'EmergencyAddressBulkDeleteView',
    'VoiceLocationListView',
    'VoiceLocationView',
    'VoiceLocationEditView',
    'VoiceLocationDeleteView',
    'VoiceLocationBulkImportView',
    'VoiceLocationBulkEditView',
    'VoiceLocationBulkDeleteView',
)


#
# Emergency Address
#

class EmergencyAddressListView(generic.ObjectListView):
    queryset = models.EmergencyAddress.objects.prefetch_related('site')
    table = tables.EmergencyAddressTable
    filterset = filtersets.EmergencyAddressFilterSet
    filterset_form = forms.EmergencyAddressFilterForm


@register_model_view(models.EmergencyAddress)
class EmergencyAddressView(generic.ObjectView):
    queryset = models.EmergencyAddress.objects.all()


@register_model_view(models.EmergencyAddress, 'edit')
class EmergencyAddressEditView(generic.ObjectEditView):
    queryset = models.EmergencyAddress.objects.all()
    form = forms.EmergencyAddressForm


@register_model_view(models.EmergencyAddress, 'delete')
class EmergencyAddressDeleteView(generic.ObjectDeleteView):
    queryset = models.EmergencyAddress.objects.all()


class EmergencyAddressBulkImportView(generic.BulkImportView):
    queryset = models.EmergencyAddress.objects.all()
    model_form = forms.EmergencyAddressImportForm


class EmergencyAddressBulkEditView(generic.BulkEditView):
    queryset = models.EmergencyAddress.objects.all()
    filterset = filtersets.EmergencyAddressFilterSet
    table = tables.EmergencyAddressTable
    form = forms.EmergencyAddressBulkEditForm


class EmergencyAddressBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EmergencyAddress.objects.all()
    filterset = filtersets.EmergencyAddressFilterSet
    table = tables.EmergencyAddressTable


#
# Voice Location
#

class VoiceLocationListView(generic.ObjectListView):
    queryset = models.VoiceLocation.objects.prefetch_related('site', 'location', 'platform', 'tenant', 'emergency_address')
    table = tables.VoiceLocationTable
    filterset = filtersets.VoiceLocationFilterSet
    filterset_form = forms.VoiceLocationFilterForm


@register_model_view(models.VoiceLocation)
class VoiceLocationView(generic.ObjectView):
    queryset = models.VoiceLocation.objects.all()


@register_model_view(models.VoiceLocation, 'edit')
class VoiceLocationEditView(generic.ObjectEditView):
    queryset = models.VoiceLocation.objects.all()
    form = forms.VoiceLocationForm


@register_model_view(models.VoiceLocation, 'delete')
class VoiceLocationDeleteView(generic.ObjectDeleteView):
    queryset = models.VoiceLocation.objects.all()


class VoiceLocationBulkImportView(generic.BulkImportView):
    queryset = models.VoiceLocation.objects.all()
    model_form = forms.VoiceLocationImportForm


class VoiceLocationBulkEditView(generic.BulkEditView):
    queryset = models.VoiceLocation.objects.all()
    filterset = filtersets.VoiceLocationFilterSet
    table = tables.VoiceLocationTable
    form = forms.VoiceLocationBulkEditForm


class VoiceLocationBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VoiceLocation.objects.all()
    filterset = filtersets.VoiceLocationFilterSet
    table = tables.VoiceLocationTable
