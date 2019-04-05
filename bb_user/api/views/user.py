import jwt
import uuid
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import make_password

from bb_user.models import AuthToken
from bb_user.api.forms.user import CreateForm, PasswordResetForm
# from utils.api.views import APIView
from utils.api.mixins import APIPermissionsMixin

from bb_user.serializers.user import CreateUserSerializer, ActivateUserSerializer


class UserCreateView(APIView):
    user_model = get_user_model()
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user = serializer.instance
        token = Token.objects.create(user=user)
        send_mail(
            'Congratulation! You are registered',
            'Hello {0}!  Login: {0}  Visit this link: http://127.0.0.1:8008/api/user/activate/?t={1}'.format(
                user.username, token.key),
            settings.ADMIN_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return Response({'Message': 'User created'}, status=status.HTTP_201_CREATED)


class UserActivateView(APIView):
    def get(self, request):
        serializer = ActivateUserSerializer()
        token = request.GET['t']
        serializer.update(token)

        return Response({'Message': 'User activated'}, status=status.HTTP_200_OK)


'''class UserRegister(APIView):

    def post(self, request, parameters, *args, **kwargs):

        form = CreateForm(data=parameters)

        if form.is_valid():
            token = uuid.uuid4()
            user = form.save(commit=False)
            user.password_reset = token
            user.save()

            send_mail(
                'Congratulation! You are registered',
                'Hello {1}!  Login: {0}  Password: {1} Visit this link: http://127.0.0.1:8008/api/user/activate/?t={2}'.format(
                    parameters['username'], parameters['password'], token),
                settings.ADMIN_EMAIL,
                [parameters['email']],
                fail_silently=False,
            )
            return JsonResponse({'message': 'User Registered, activate'}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse(errors, status=500, safe=False)

    def get(self, request, *args, **kwargs):
        # todo: this is for example how to call user model!
        user_model = get_user_model()
        user = user_model.objects.get(id=1)
        return {'message': 'Register'}


class UserActivate(APIView):
    def get(self, request, parameters):
        try:
            user = self.user_model.objects.get(password_teset=parameters['t'])
        except user.DoesNotExist:
            return JsonResponse({'message': 'Invalid token'}, status=400)
        user.is_blocked = False
        user.password_reset = None
        user.save()
        return JsonResponse({'message': 'User Activated'}, status=200)


class UserLogin(APIView):
    need_auth = True

    def post(self, request, parameters, *args, **kwargs):

        if not self.access_token:
            return self.login_with_username_and_password(parameters)

        user = self.user_model.objects.get(pk=self.session.user.id)
        if user.is_blocked:
            return JsonResponse({'Message': 'Activate your account'}, status=403)
        login(request, user)
        return JsonResponse({'Message': 'You Are Logged In'}, status=200)

    def login_with_username_and_password(self, parameters):

        if not authenticate(username=parameters['username'], password=parameters['password']):
            return JsonResponse({
                'message': 'Wrong Username or Password'
            }, status=400)

        user = self.user_model.objects.get(usename=parameters['username'])

        if user.is_blocked:
            return JsonResponse({'Message': 'Activate your account'}, status=403)
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
            user.password = make_password(parameters['password'])
            user.password_reset = None
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
        return JsonResponse({'message': 'access denied'}, status=403)'''
