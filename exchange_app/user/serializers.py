from rest_framework import serializers
from exchange_app.user.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'