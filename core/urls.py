from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^$', 'core.views.index_page', name='index'),
#    url(r'^about/', 'core.views.about_page', name='about'),
#    url(r'^contact/', 'core.views.contact_page', name='contact'),
    
    #url(r'^build/', include('build.urls')),
    url(r'^polls/', include('apps.polls.urls', namespace="polls")),
    
    url(r'^admin/', include(admin.site.urls)),
)
