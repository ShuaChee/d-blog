from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^posts', include('bb_post.api.urls')),
    ])),
]
