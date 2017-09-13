from django.conf.urls import patterns, include, url

from .views import post


urlpatterns = patterns('',
    url('^post', include(patterns('',
        url(r'^$', post.List.as_view(), name='list'),
        url(r'^/(?P<post_id>\d+)$', post.View.as_view(), name='view'),
    ), namespace='post')),
)
