from rest_framework import serializers
from parks.serializers import ParkNameSerializer, TrailSummarySerializer
from .models import Hiker, Hike

class HikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiker
        fields = ['id', 'name', 'email', 'username', 'registered']

class HikeSerializer(serializers.ModelSerializer):
    park_id = ParkNameSerializer(many=False)
    trails = TrailSummarySerializer(many=True)

    class Meta:
        model = Hike
        fields = ['id', 'hiker_id', 'park_id', 'date', 'distance', 'notes', 'trails']