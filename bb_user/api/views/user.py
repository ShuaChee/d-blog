import jwt
import uuid
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

from bb_user.serializers.user import CreateUserSerializer, ActivateUserSerializer, ResetUserPasswordSerializer


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


class UserResetPassword(APIView):
    serializer = ResetUserPasswordSerializer()

    def get(self, request, *args, **kwargs):
        response = self.serializer.get_reset_token(request.GET['userid'])
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        response = self.serializer.reset_password(request.body)
        return Response(response, status=status.HTTP_200_OK)
