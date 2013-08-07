from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # global urls
    url(r'^bart/', 'bart.views.index_page', name='index'),
    #url(r'^about/', 'static.views.about_page', name='about'),
    #url(r'^contact/', 'static.views.contact_page', name='contact'),
    
    url(r'^build/', include('build.urls')),
    #url(r'^audit/', include('audit.urls')),
    #url(r'^report/', include('reports.urls')),
    #url(r'^test/', include('devtest.urls')),
    
    # ip_addresses application
    url(r'^ip_addresses/', include('ip_addresses.urls')),
    
    # admin application
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
