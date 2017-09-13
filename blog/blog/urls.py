from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('interface.urls', namespace='interface')),
)
