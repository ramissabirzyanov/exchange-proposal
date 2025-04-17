from rest_framework import serializers
from exchange_app.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
