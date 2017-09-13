from django.conf.urls import patterns, url

from .views import post


urlpatterns = patterns('',
    url(r'^$', post.Collection.as_view()),
    url(r'^/(?P<post_id>\d+)$', post.Single.as_view()),
)
