from django.conf.urls import include, url

from .views import post


urlpatterns = [
    url('^post', include([
        url(r'^$', post.List.as_view(), name='list'),
        url(r'^/(?P<post_id>\d+)$', post.View.as_view(), name='view'),
    ]))
]
