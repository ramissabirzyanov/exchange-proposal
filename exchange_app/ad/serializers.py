from rest_framework import serializers
from exchange_app.ad.models import Ad


class AdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ad
        fields = '__all__'