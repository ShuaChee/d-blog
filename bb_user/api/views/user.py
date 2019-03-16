from django.views.generic import View, CreateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegister(CreateView):
    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        print(user)
        return HttpResponse('Register')


class UserLogin(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Login')


class UserLogout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Logout')
