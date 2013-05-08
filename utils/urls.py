from django.conf.urls import patterns,  url

from utils.views import DocsView


urlpatterns = patterns('',
    url(r'^about/$', DocsView.as_view(), name='about'),
    url(r'^about/(?P<name>.+)', DocsView.as_view(), name='about'),
)