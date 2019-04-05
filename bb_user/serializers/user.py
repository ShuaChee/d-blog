from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model


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
        except Token.DoesNotExist:
            raise serializers.ValidationError({'password': 'Invalid token'})
        user = token.user
        user.is_active = True
        user.save()
        token.delete()
        return user

