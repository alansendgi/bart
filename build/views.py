from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from build.models import NetworkDevice
import forms


class ListNetworkDeviceView(ListView):
    
    model = NetworkDevice
    template_name = 'networkdevice_list.html'
    
    
class NetworkDeviceView(DetailView):
    
    model = NetworkDevice
    template_name = 'networkdevice.html'
    
    
class CreateNetworkDeviceView(CreateView):
    
    model = NetworkDevice
    template_name = 'edit_networkdevice_custom.html'
    form_class = forms.NetworkDeviceForm
    
    def get_success_url(self):
        return reverse('networkdevices-list')
    
    def get_context_data(self, **kwargs):

        context = super(CreateNetworkDeviceView, self).get_context_data(**kwargs)
        context['action'] = reverse('networkdevices-new')

        return context


class UpdateNetworkDeviceView(UpdateView):

    model = NetworkDevice
    template_name = 'edit_networkdevice.html'
    form_class = forms.NetworkDeviceForm

    def get_success_url(self):
        return reverse('networkdevices-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateNetworkDeviceView, self).get_context_data(**kwargs)
        context['action'] = reverse('networkdevices-edit',
                                    kwargs={'pk': self.get_object().id})

        return context


class DeleteNetworkDeviceView(DeleteView):

    model = NetworkDevice
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('networkdevices-list')


class EditNetworkDeviceAddressView(UpdateView):

    model = NetworkDevice
    template_name = 'edit_addresses.html'
    form_class = forms.NetworkDeviceAddressFormSet

    def get_success_url(self):

        # redirect to the NetworkDevice view.
        return self.get_object().get_absolute_url()
