import jwt
import uuid
from datetime import datetime

from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import make_password

from bb_user.models import AuthToken
from bb_user.api.forms.user import CreateForm, PasswordResetForm
from utils.api.views import APIView
from utils.api.mixins import APIPermissionsMixin


class UserRegister(APIView):

    def post(self, request, parameters, *args, **kwargs):

        form = CreateForm(data=parameters)

        if form.is_valid():
            form.save()
            send_mail(
                'Congratulation! You are registered',
                'Hello {1}! /n Login: {0} /n Password: {1}'.format(parameters['username'], parameters['password']),
                settings.ADMIN_EMAIL,
                [parameters['email']],
                fail_silently=False,
            )
            return JsonResponse({'message': 'User Registered'}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse(errors, status=500, safe=False)

    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        return {'message': 'Register'}


class UserLogin(APIView):
    need_auth = True

    def post(self, request, parameters, *args, **kwargs):

        if not self.access_token:
            return self.login_with_username_and_password(parameters)

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
            access_token = jwt.encode({'user_id': user.id, 'login_time': str(datetime.now())}, settings.SECRET_KEY,
                                      algorithm='HS256')
            session = AuthToken.objects.create(
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


class UserResetPassword(APIView):
    def post(self, request, parameters, *args, **kwargs):
        form = PasswordResetForm(data=parameters)
        try:
            user = self.user_model.objects.get(password_reset=parameters['reset_token'])
        except self.user_model.DoesNotExist:
            return JsonResponse({
                'message': 'Token not found'
            }, status=404)
        if form.is_valid():
            user.password = parameters['password']
            user.save()
            return JsonResponse({
                'message': 'Done'
            }, status=200)

    def get(self, request, parameters, *args, **kwargs):
        try:
            user = self.user_model.objects.get(username=parameters['username'])
        except self.user_model.DoesNotExist:
            return JsonResponse({
                'message': 'User not found'
            }, status=404)
        token = uuid.uuid4()
        user.password_reset = token
        user.save()
        return JsonResponse({
            'reset_token': token
        }, status=200)


class UserBlock(APIPermissionsMixin, APIView):
    def post(self, request, parameters, *args, **kwargs):
        access_token = self.get_access_token(request)
        if self.has_permissions(access_token):
            try:
                user = self.user_model.objects.get(pk=int(parameters['user_id']))
            except self.user_model.DoesNotExist:
                return JsonResponse({'message': 'User not found'}, status=404)
            user.is_blocked = True
            user.save()
            return JsonResponse({'message': 'done'}, status=200)
        return JsonResponse({'message': 'access denied'}, status=403)
