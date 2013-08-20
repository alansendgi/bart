# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^home/',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),
    url(r'^contact/',
        TemplateView.as_view(template_name='pages/contact.html'),
        name="contact"),
    
    
    url(r'^build/', include('build.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
