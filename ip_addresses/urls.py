from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse

from ip_addresses.models import *
import ip_addresses.views as views

classrule_form = {
    'form_class': ClassRuleForm,
    'template_name': 'ip_addresses/add.html',
}

classrule_delete = {
    'model': ClassRule,
    'post_delete_redirect': '../..',
    'template_name': 'ip_addresses/delete_confirm_classrule.html',
}

urlpatterns = patterns('',
    url(r'^networkaddress/$', views.networkaddress_display, name='networkaddress-displaytop'),
    url(r'^networkaddress/add/$', views.networkaddress_add, name='networkaddress-addtop'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/$', views.networkaddress_display, name='networkaddress-display'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/delete/$', views.networkaddress_delete, name='networkaddress-delete'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/add/$', views.networkaddress_add, name='networkaddress-add'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/modify/$', views.networkaddress_modify, name='networkaddress-modify'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/add_dhcp/$', views.dhcpnetwork_add, name='networkaddress-adddhcp'),
    url(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/ping/$', views.networkaddress_ping, name='networkaddress-ping'),
    url(r'^networkaddress/$', views.networkaddress_ping, name='networkaddress-ping-url'),

    url(r'^dhcpnetwork/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/$', views.dhcpnetwork_display, name='dhcpnetwork-display'),
    url(r'^dhcpnetwork/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/delete/$', views.dhcpnetwork_delete, name='dhcpnetwork-delete'),
    url(r'^dhcpnetwork/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/modify/$', views.dhcpnetwork_modify, name='dhcpnetwork-modify'),
    url(r'^dhcpnetwork/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/add_dhcppool/$', views.dhcpaddresspool_add, name='dhcpnetwork-addpool'),

    url(r'^dhcpaddresspool/add/$', views.dhcpaddresspool_add),
    url(r'^dhcpaddresspool/(?P<range_start>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/(?P<range_finish>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$', views.dhcpaddresspool_display, name='dhcpaddresspool-display'),
    url(r'^dhcpaddresspool/(?P<range>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/delete/$', views.dhcpaddresspool_delete, name='dhcpaddresspool-delete'),

    url(r'^classrule/$', ListView.as_view(queryset=ClassRule.objects.all(), template_name='ip_addresses/display_classrule.html'), name='classrule-displaytop'),
    url(r'^classrule/(?P<object_id>\d+)/$', ListView.as_view(queryset=ClassRule.objects.all(), template_name='ip_addresses/display_classrule.html'), name='classrule-display'),
    url(r'^classrule/(?P<object_id>\d+)/modify/$', UpdateView.as_view(), classrule_form, name='classrule-modify'),
    url(r'^classrule/(?P<object_id>\d+)/delete/$', DeleteView.as_view(), classrule_delete, name='classrule-delete'),
    url(r'^classrule/add/$', CreateView.as_view(), classrule_form, name='classrule-add'),

    url(r'^dhcpd.conf/$', views.dhcpd_conf_generate, name='dhcp-conf-generate'),

# NETWORKDEVICE urls

    url(r'^networkdevice/$', views.networkdevice_display, name='networkdevice-displaytop'),
    url(r'^networkdevice/add/$', views.networkdevice_add, name='networkdevice-addtop'),
    url(r'^networkdevice/delete/$', views.networkdevice_delete, name='networkdevice-delete'),
    url(r'^networkdevice/modify/$', views.networkdevice_modify, name='networkdevice-modify'),
#    url(r'^networkdevice/ping/$', views.networkdevice_ping, name='networkdevice-ping'),
)
