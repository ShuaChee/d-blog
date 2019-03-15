from django.conf.urls import url

from .views import user


urlpatterns = [
    url(r'^/create', user.UserRegister.as_view()),
    url(r'^/login', user.UserLogin.as_view()),
    url(r'^/logout', user.UserLogout.as_view()),
]
