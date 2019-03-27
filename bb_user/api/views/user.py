from django.http import JsonResponse
from django.views.generic import View
from utils.api.mixins import APIMixin
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password


class UserRegister(APIMixin, View):

    def post(self, request, parameters, *args, **kwargs):
        user_model = get_user_model()

        if parameters['password'] != parameters['confirm_password']:
            return {'message': 'Check password'}

        try:
            user = user_model.objects.create(
                username=parameters['username'],
                password=make_password(parameters['password']),
                email=parameters['email']
            )
            user.save()
            return {'message': 'User Registered'}
        except:
            return {'message': 'Email or username already taken'}

    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        return {'message': 'Register'}


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
                'message': 'You are logged in',
                'session_key': request.session.session_key
            }


class UserLogout(APIMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return {
                'message': 'Logged out'
            }
