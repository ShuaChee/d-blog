from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^api/', include(patterns('',
        url(r'^posts', include('bb_post.api.urls')),
    ))),
)
