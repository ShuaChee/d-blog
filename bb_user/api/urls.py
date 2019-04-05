from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from bb_user.api.views import user


urlpatterns = [
    path('create/', user.UserCreateView.as_view()),
    # path('login/', user.UserLogin.as_view(), name='login'),
    path('login/', obtain_auth_token, name='token_auth'),
    # path('logout/', user.UserLogout.as_view()),
    # path('block/', user.UserBlock.as_view()),
    path('activate/', user.UserActivateView.as_view()),
    path('reset/', user.UserResetPassword.as_view())
]
