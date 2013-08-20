# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from build.models import NetworkAddress
import forms


class ListNetworkAddressView(ListView):

    model = NetworkAddress
    template_name = 'build/networkaddress_list.html'
    
    
class CreateNetworkAddressView(CreateView):

    model = NetworkAddress
    template_name = 'build/networkaddress_edit.html'

    def get_success_url(self):
        return reverse('networkaddress-list')
    
    def get_context_data(self, **kwargs):
        
        context = super(CreateNetworkAddressView, self).get_context_data(**kwargs)
        context['action'] = reverse('networkaddress-new')
        
        return context
        
    
class UpdateNetworkAddressView(UpdateView):

    model = NetworkAddress
    template_name = 'build/networkaddress_edit.html'

    def get_success_url(self):
        return reverse('networkaddress-list')
    
    def get_context_data(self, **kwargs):
        
        context = super(UpdateNetworkAddressView, self).get_context_data(**kwargs)
        context['action'] = reverse('networkaddress-edit',
                                    kwargs={'pk': self.get_object().id})
        
        return context
    
    
class DeleteNetworkAddressView(DeleteView):
    
    model = NetworkAddress
    template_name = 'build/networkaddress_delete.html'

    def get_success_url(self):
        return reverse('networkaddress-list')
        

class NetworkAddressView(DetailView):

    model = NetworkAddress
    template_name = 'build/networkaddress.html'

    def get_success_url(self):
        return reverse('networkaddress-list')
    

class EditNetworkDeviceView(UpdateView):
    
    model = NetworkAddress
    template_name = 'build/networkdevice_edit.html'
    form_class = forms.NetworkDeviceFormSet
    
    def get_success_url(self):
        
        # redirect to the NetworkAddress view.
        return self.get_object().get_absolute_url()
