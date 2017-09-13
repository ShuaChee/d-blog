from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(patterns('',
        url(r'^posts', include('bb_post.api.urls')),
    ))),
)
