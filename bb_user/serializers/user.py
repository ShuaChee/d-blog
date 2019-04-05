import json
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'confirm_password', 'email', 'auth_token')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        if validated_data.get('password') != confirm_password:
            raise serializers.ValidationError({'password': 'Check password'})
        model = get_user_model()
        user = model.objects.create_user(**validated_data)
        user.is_active = False
        return user


class ActivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['is_active', 'auth_token']

    def update(self, token):
        try:
            token = Token.objects.get(key=token)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'password': 'Invalid token'})
        user = token.user
        user.is_active = True
        user.save()
        token.delete()
        return user


class ResetUserPasswordSerializer(serializers.ModelSerializer):
    user_model = get_user_model()

    class Meta:
        model = get_user_model()
        fields = ['password', 'auth_token']

    def get_reset_token(self, email):
        try:
            user = self.user_model.objects.get(email=email)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'user': 'User not found'})

        try:
            token = Token.objects.get(user=user)
            token.delete()
        except Token.DoesNotExist:
            pass

        token = Token.objects.create(user=user)

        send_mail(
            'Password reset link',
            'Reset link: http://front.com/api/user/reset/?t={0}'.format(
                token.key),
            settings.ADMIN_EMAIL,
            [email],
            fail_silently=False,
        )
        return {"Message": "Reset link sent"}

    def reset_password(self, data):
        data = json.loads(data)
        try:
            token = Token.objects.get(key=data['reset_token'])
        except ObjectDoesNotExist:
            serializers.ValidationError({'reset_token': 'Invalid token'})

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Check password'})

        user = token.user
        token.delete()
        user.password = make_password(data['password'])
        return {'Message': 'Password changed'}


class UserBlockSerializer(serializers.ModelSerializer):
    user_model = get_user_model()

    def block_user(self, user_id):
        try:
            user = self.user_model.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return {'Message': 'User Not Found'}, 404

        user.is_blocked = True
        user.save()
        return {'Message': 'User blocked'}, 200
