from django.urls import path

from bb_user.api.views import user


urlpatterns = [
    path('create/', user.UserRegister.as_view()),
    path('login/', user.UserLogin.as_view()),
    path('logout/', user.UserLogout.as_view()),
]
