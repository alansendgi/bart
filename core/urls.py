from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^bart/', 'bart.views.index_page', name='index'),
    url(r'^build/', include('build.urls')),
)
