# -*- coding: utf-8 -*-
from build.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import subprocess

# NETWORKADDRESS view functions

def networkaddress_display(request, address=None):
    parent = get_network_object_from_address(address)
    addr_list = NetworkAddress.objects.filter(parent=parent)
    has_subnets = False
    for address in addr_list:
        if address.network_size != 32:
            has_subnets = True
    try:
        dhcp_net = DHCPNetwork.objects.get(physical_net=parent)
    except:
        dhcp_net = None
    return render_to_response('build/display.html', {'parent': parent, 
                                               'addresses_list': addr_list, 
                                               'has_subnets': has_subnets,
                                               'dhcp_net': dhcp_net,})

def networkaddress_delete(request, address=None):
    address_obj = get_network_object_from_address(address)
    parent = address_obj.parent
    address_obj.delete()
    redirect_to = '../../../'
    if parent:
        redirect_to = parent.get_absolute_url()
    return HttpResponseRedirect(redirect_to)

def networkaddress_add(request, address=None):
    if request.method == 'POST':
        parent = get_network_object_from_address(address)
        new_address = NetworkAddress(parent=parent)
        form = NetworkAddressAddForm(request.POST, instance=new_address)
        if form.is_valid():
            form.save()
            url = parent.get_absolute_url() if parent else reverse('networkaddress-displaytop')
            return HttpResponseRedirect(url)
    else:
        form = NetworkAddressAddForm()
    return render_to_response('build/add.html', {'form': form,}, context_instance=RequestContext(request))    

def networkaddress_modify(request, address=None):
    address_obj = get_network_object_from_address(address)
    if request.method == 'POST':
        # submitting changes
        form = NetworkAddressModifyForm(request.POST, instance=address_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(address_obj.parent.get_absolute_url())
    else:
        # first time display
        form = NetworkAddressModifyForm(initial={ 'description': address_obj.description, })
    return render_to_response('build/add.html', {'form': form,}, context_instance=RequestContext(request))

def networkaddress_ping(request, address=None):
    if responding_to_ping(address):
        msg = "Ping OK"
    else:
        msg = "No response"
    return HttpResponse(msg)



# NETWORKDEVICE view functions

def networkdevice_display(request, device=None):
    ##parent = get_network_object_from_device(device)
    device_list = NetworkDevice.objects.all()
    return render_to_response('build/display_device.html', {'device_list': device_list,})

def networkdevice_delete(request, device=None):
    device_obj = get_network_object_from_device(device)
    parent = device_obj.parent
    device_obj.delete()
    redirect_to = '../../../'
    if parent:
        redirect_to = parent.get_absolute_url()
    return HttpResponseRedirect(redirect_to)

def networkdevice_add(request, device=None):
    if request.method == 'POST':
        ##parent = get_network_object_from_device(device)
        new_device = NetworkDevice()
        form = NetworkDeviceAddForm(request.POST, instance=new_device)
        if form.is_valid():
            form.save()
            url = reverse('networkdevice-displaytop')
            return HttpResponseRedirect(url)
    else:
        form = NetworkDeviceAddForm()
    return render_to_response('build/add.html', {'form': form,}, context_instance=RequestContext(request))    

def networkdevice_modify(request, device=None):
    device_obj = NetworkDevice(device)
    if request.method == 'POST':
        form = NetworkDeviceModifyForm(request.POST, instance=device_obj)
        if form.is_valid():
            form.save()
            url = reverse('networkdevice-displaytop')
            return HttpResponseRedirect(url)
    else:
        # first time display
        form = NetworkDeviceModifyForm(initial={ 'description': device_obj.description, })
    return render_to_response('build/add.html', {'form': form,}, context_instance=RequestContext(request))


############################################################################
# helper functions

def get_network_object_from_address(address):
    if address:
        ip, net_size = address.split('/')
        object = NetworkAddress.objects.get(address=ip, network_size=int(net_size))
    else:
        object = None
    return object

def responding_to_ping(address, timeout=1):
    rc = subprocess.call("ping -c 1 -W %d %s" % (timeout, address), 
                         shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
    if rc == 0:
        return True
    else:
        return False
