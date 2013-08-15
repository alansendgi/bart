from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^bart/', 'bart.views.index_page', name='index'),
    url(r'^build/', include('build.urls')),
    
    url(r'.*', RedirectView.as_view(url='/bart/')),
)
