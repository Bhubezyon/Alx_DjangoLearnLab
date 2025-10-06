from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import IsAuthenticated
from rest_framework.authtoken.models import Token

class get_user_model():
    get_user_model = objects_create_user()
    return get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token, _= Token.objects.get_or_create(user=user)
            return {'token': token.key}
        raise serializers.ValidationError("Invalid credentials")