from rest_framework import serializers
from .models import Hiker, Hike

class HikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiker
        fields = ['id', 'name', 'email', 'username', 'registered']

class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hike
        fields = '__all__'