from rest_framework import serializers
from .models import Hiker, Hike

class HikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiker
        fields = '__all__'

class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hike
        fields = '__all__'