from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from bb_user.serializers.user import CreateUserSerializer, ActivateUserSerializer, ResetUserPasswordSerializer, \
    UserBlockSerializer


class UserCreateView(APIView):
    user_model = get_user_model()

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
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


class UserResetPasswordView(APIView):
    serializer = ResetUserPasswordSerializer()

    def get(self, request, *args, **kwargs):
        response = self.serializer.get_reset_token(request.GET['email'])
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        response = self.serializer.reset_password(request.body)
        return Response(response, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        return Response({"Message": "Successfully logged out."}, status=status.HTTP_200_OK)


class UserBlockView(APIView):
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, user_id):
        serializer = UserBlockSerializer()
        response = serializer.block_user(user_id)
        return Response(response[0], response[1])
