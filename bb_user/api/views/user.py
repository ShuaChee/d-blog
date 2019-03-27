from django.http import JsonResponse
from django.views.generic import View
from utils.api.mixins import APIMixin
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password


class UserRegister(APIMixin, View):

    def post(self, request, parameters, *args, **kwargs):
        password = parameters['password']
        confirm_password = parameters['confirm_password']
        email = parameters['email']
        username = parameters['username']
        user_model = get_user_model()

        if password != confirm_password:
            return HttpResponse('Check password')

        try:
            user = user_model.objects.create(
                username=username,
                password=make_password(password),
                email=email
            )
            user.save()
            return {
                'message': 'User Registered'
            }
        except:
            return {
                'message': 'Email or username already taken'
            }

    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        return HttpResponse('Register')


class UserLogin(APIMixin, View):
    def post(self, request, parameters, *args, **kwargs):
        user = authenticate(username=parameters['username'], password=parameters['password'])

        if user is None:
            return {
                'message': 'Wrong Username or Password'
            }
        else:
            login(request, user)
            return {
                'message': 'You are logged in'
            }


class UserLogout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({
                'message': 'Logged out'
            })
