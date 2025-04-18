from rest_framework import serializers

from exchange_app.ad.models import Ad
from exchange_app.user.serializers import UserSerializer

class AdSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    title = serializers.CharField(default="")
    description = serializers.CharField(default="", allow_blank=True)
    image_url = serializers.CharField(default="", allow_blank=True)
    condition = serializers.CharField(default="", allow_blank=True)
    
    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ('owner',)

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
