# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

import build.views


urlpatterns = patterns('',
    url(r'^$', build.views.ListNetworkAddressView.as_view(),
        name='networkaddress-list',),
    url(r'^(?P<pk>\d+)/$', build.views.NetworkAddressView.as_view(),
        name='networkaddress-view',),
    url(r'^new$', build.views.CreateNetworkAddressView.as_view(),
        name='networkaddress-new',),
    url(r'^edit/(?P<pk>\d+)/$', build.views.UpdateNetworkAddressView.as_view(),
        name='networkaddress-edit',),
    url(r'^edit/(?P<pk>\d+)/networkdevice$', build.views.EditNetworkDeviceView.as_view(),
        name='networkdevice-edit',),
    url(r'^delete/(?P<pk>\d+)/$', build.views.DeleteNetworkAddressView.as_view(),
        name='networkaddress-delete',),
)
