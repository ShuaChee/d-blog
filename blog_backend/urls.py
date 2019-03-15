from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^posts', include('bb_post.api.urls')),
        url(r'^user', include('bb_user.api.urls')),
    ])),
]
