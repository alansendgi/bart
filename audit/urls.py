from django.conf.urls import patterns, url

from audit import views

urlpatterns = patterns('',
    url(r'^$', views.audit_main, name='network-audit')
)
