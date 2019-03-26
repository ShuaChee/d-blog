from django.urls import path

from bb_user.api.views import user


urlpatterns = [
    path('create/', user.UserRegister.as_view(), name='create'),
    path('login/', user.UserLogin.as_view(), name='login'),
    path('logout/', user.UserLogout.as_view()),
]
