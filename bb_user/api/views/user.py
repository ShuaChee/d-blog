import json
from django.views.generic import View, CreateView
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from bb_user.models import User


class UserRegister(CreateView):
    model = User

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        password = data['password']
        confirm_password = data['confirm_password']
        email = data['email']
        username = data['username']
        user_model = get_user_model()

        if password != confirm_password:
            return HttpResponse('Check password')

        try:
            user = user_model.objects.create(
                username=username,
                password=password,
                email=email
            )
            user.save()
            return HttpResponse('User registered')
        except:
            return HttpResponse('Email or username already taken')

    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        return HttpResponse('Register')


class UserLogin(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])

        if user is None:
            return HttpResponse('Wrong Username or Password')
        else:
            login(request, user)
            return HttpResponse('U R logged In')


class UserLogout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Logout')
