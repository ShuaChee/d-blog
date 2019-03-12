from django.conf.urls import url

from .views import post


urlpatterns = [
    url(r'^$', post.Collection.as_view()),
    url(r'^/(?P<post_id>\d+)$', post.Single.as_view()),
]
