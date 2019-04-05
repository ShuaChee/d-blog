from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from bb_user.api.views import user


urlpatterns = [
    path('create/', user.UserCreateView.as_view()),
    path('login/', obtain_auth_token, name='token_auth'),
    path('logout/', user.UserLogoutView.as_view()),
    path('block/<user_id>/', user.UserBlockView.as_view()),
    path('activate/', user.UserActivateView.as_view()),
    path('reset/', user.UserResetPasswordView.as_view())
]
