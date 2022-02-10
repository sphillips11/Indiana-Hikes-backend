from rest_framework import serializers
from .models import Park, Trail

class ParkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ['name', 'slug', 'city', 'state', 'accessible_trails', 'easy_trails', 'moderate_trails', 'difficult_trails', 'more_difficult_trails', 'moderately_rugged', 'rugged_trails', 'very_rugged_trails', 'accessibility', 'challenge']

class ParkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'