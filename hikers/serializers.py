from rest_framework import serializers
from parks.serializers import ParkNameSerializer, TrailSummarySerializer
from .models import Hiker, Hike

class HikerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiker
        fields = '__all__'

class HikeSerializer(serializers.ModelSerializer):
    park_id = ParkNameSerializer(many=False)
    trails = TrailSummarySerializer(many=True)

    class Meta:
        model = Hike
        fields = ['id', 'hiker_id', 'park_id', 'date', 'distance', 'notes', 'trails']

class TrailsByParkHikerSerializer(serializers.ModelSerializer):
    trails = TrailSummarySerializer(many=True)
    
    class Meta:
        model = Hike
        fields = ['trails']