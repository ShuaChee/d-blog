from django.views.generic import View, CreateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


class UserRegister(CreateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Register')


class UserLogin(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Login')


class UserLogout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Logout')
