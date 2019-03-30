import json
import jwt
from datetime import datetime, timezone

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from bb_user.models import UserSessions


class APIView(View):
    user_model = get_user_model()

    def get_access_token(self, request):
        try:
            access_token = request.META['HTTP_AUTHORIZATION']
        except KeyError:
            access_token = None
        return access_token

    def get_user_session(self, access_token):
        try:
            session = UserSessions.objects.get(access_token=access_token)
        except UserSessions.DoesNotExist:
            return False
        return session

    def access_token_is_expired(self, access_token):
        session = UserSessions.objects.get(access_token=access_token)
        if session.expired_at < datetime.now(timezone.utc):
            return True
        return False

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
        self.access_token = self.get_access_token(request)
        self.session = self.get_user_session(self.access_token)
        try:
            result = super(APIView, self).dispatch(request, parameters=self.get_parameters(request), *args, **kwargs)
        except:
            return JsonResponse({'Message': 'Something wrong'}, status=500)
        return result


class UserRegister(APIView):

    def post(self, request, parameters, *args, **kwargs):

        if parameters['password'] != parameters['confirm_password']:
            return JsonResponse({'message': 'Check password'}, status=400)

        if self.user_model.objects.filter(username=parameters['username']):
            return JsonResponse({'message': 'Username already taken'}, status=400)

        if self.user_model.objects.filter(email=parameters['email']):
            return JsonResponse({'message': 'Email already taken'}, status=400)

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

        if not self.access_token:
            return self.login_with_username_and_password(parameters)

        if not self.session:
            return JsonResponse({'Message': 'Invalid Token'}, status=403)

        if self.access_token_is_expired(self.access_token):
            return JsonResponse({'Message': 'Relogin Please'}, status=403)

        user = self.user_model.objects.get(pk=self.session.user.id)
        login(request, user)
        return JsonResponse({'Message': 'You Are Logged In'}, status=200)

    def login_with_username_and_password(self, parameters):
        user = authenticate(username=parameters['username'], password=parameters['password'])
        if user is None:
            return JsonResponse({
                'message': 'Wrong Username or Password'
            }, status=400)
        else:
            access_token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, algorithm='HS256')
            session = UserSessions.objects.create(
                user=user,
                access_token=access_token.decode('utf-8')
            )
            session.save()
            return JsonResponse({
                'message': 'You are logged in',
                'access_token': access_token.decode('utf-8')
            }, status=200)


class UserLogout(APIView):
    def post(self, request, *args, **kwargs):
        if self.session:
            self.session.delete()
        return JsonResponse({'message': 'Logged out'}, status=200)
