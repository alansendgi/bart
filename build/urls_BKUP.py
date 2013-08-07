from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import build.views


urlpatterns = patterns('',
    url(r'^$', build.views.ListNetworkDeviceView.as_view(),
        name='networkdevices-list',),
    url(r'^(?P<pk>\d+)/$', build.views.NetworkDeviceView.as_view(),
        name='networkdevices-view',),
    url(r'^new$', build.views.CreateNetworkDeviceView.as_view(),
        name='networkdevices-new',),
    url(r'^edit/(?P<pk>\d+)/$', build.views.UpdateNetworkDeviceView.as_view(),
        name='networkdevices-edit',),
    url(r'^edit/(?P<pk>\d+)/addresses$', build.views.EditNetworkDeviceAddressView.as_view(),
        name='networkdevices-edit-addresses',),
    url(r'^delete/(?P<pk>\d+)/$', build.views.DeleteNetworkDeviceView.as_view(),
        name='networkdevices-delete',),
)

urlpatterns += staticfiles_urlpatterns()
