from django.urls import path

from .views import post

urlpatterns = [
    path('', post.Collection.as_view()),
    path('<int:post_id>/', post.Single.as_view()),
]
