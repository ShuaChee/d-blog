from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from bb_user.api import views


urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('login/', obtain_auth_token, name='token_auth'),
    path('logout/', views.UserLogoutView.as_view()),
    path('block/<user_id>/', views.UserBlockView.as_view()),
    path('activate/', views.UserActivateView.as_view()),
    path('reset/', views.UserResetPasswordView.as_view())
]
