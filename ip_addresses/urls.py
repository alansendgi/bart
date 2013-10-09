from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse

from ip_addresses.models import *
import ip_addresses.views as views

urlpatterns = patterns('',
    url(r'^networkaddress/$', views.networkaddress_display, name='networkaddress-displaytop'),
    url(r'^networkaddress/add/$', views.networkaddress_add, name='networkaddress-addtop'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/$', views.networkaddress_display, name='networkaddress-display'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/delete/$', views.networkaddress_delete, name='networkaddress-delete'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/add/$', views.networkaddress_add, name='networkaddress-add'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/modify/$', views.networkaddress_modify, name='networkaddress-modify'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/ping/$', views.networkaddress_ping, name='networkaddress-ping'),
    url(r'^networkaddress/$', views.networkaddress_ping, name='networkaddress-ping-url'),

# NETWORKDEVICE urls

    url(r'^networkdevice/$', views.networkdevice_display, name='networkdevice-displaytop'),
    url(r'^networkdevice/add/$', views.networkdevice_add, name='networkdevice-addtop'),
    url(r'^networkdevice/delete/$', views.networkdevice_delete, name='networkdevice-delete'),
    url(r'^networkdevice/modify/$', views.networkdevice_modify, name='networkdevice-modify'),
)
