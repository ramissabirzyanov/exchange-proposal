from rest_framework import serializers
from rest_framework.validators import ValidationError
from exchange_app.user.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(default="", allow_blank=True)
    last_name = serializers.CharField(default="", allow_blank=True)

    class Meta:
        model = User
        fields =  ['id', 'first_name', 'last_name']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password2'}
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError({"password": "Пароли не совпадают"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
