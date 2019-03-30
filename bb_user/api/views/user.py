import json
import jwt
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from utils.api.mixins import APIMixin
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from bb_user.models import UserSessions


class APIView(View):

    user_model = get_user_model()

    def get_parameters(self, request):
        parameters = {}
        try:
            if request.method in ('POST', 'PUT'):
                parameters = json.loads(request.body)

            if request.method == 'GET':
                parameters = request.GET

        except:
            return JsonResponse({'Message': 'Load Data Error'}, status=500)

        return parameters

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        try:
            result = super(APIView, self).dispatch(request, parameters=self.get_parameters(request), *args, **kwargs)
        except:
            return JsonResponse({'Message': 'Something wrong'}, status=500)
        return result


class UserRegister(APIView):

    def post(self, request, parameters, *args, **kwargs):

        if parameters['password'] != parameters['confirm_password']:
            return JsonResponse({'message': 'Check password'}, status=200)

        if self.user_model.objects.filter(username=parameters['username']):
            return JsonResponse({'message': 'Username already taken'}, status=200)

        if self.user_model.objects.filter(email=parameters['email']):
            return JsonResponse({'message': 'Email already taken'}, status=200)

        user = self.user_model.objects.create(
            username=parameters['username'],
            password=make_password(parameters['password']),
            email=parameters['email']
        )
        user.save()
        return JsonResponse({'message': 'User Registered'}, status=200)


    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        return {'message': 'Register'}


class UserLogin(APIView):
    def post(self, request, parameters, *args, **kwargs):

        access_token = request.META.get('Authorization')
        if access_token:
            try:
                session = UserSessions.objects.get(access_token=token)
            except UserSessions.DoesNotExist:
                return JsonResponse({'Message': 'Invalid Token'}, status=403)

            if session.expired_at < datetime.now:
                return JsonResponse({'Message': 'Token Expired'}, status=403)
            else:
                user = self.user_model.objects.get(pk=session.user)
                login(request, user)
                return JsonResponse({'Message': 'U R Logged In'}, status=200)


        user = authenticate(username=parameters['username'], password=parameters['password'])

        if user is None:
            return JsonResponse({
                'message': 'Wrong Username or Password'
            }, status=403)
        else:
            access_token = 123 #jwt.encode({'user_id': user.id}, settings['SECRET_KEY'], algorithm='HS256')
            session = UserSessions.objects.create(
                user=user.id,
                access_token=access_token
            )
            session.save()
            return JsonResponse({
                'message': 'You are logged in',
                'access_token': access_token
            }, status=200)


class UserLogout(APIMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return {
            'message': 'Logged out'
        }
