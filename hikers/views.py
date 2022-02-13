from cgitb import lookup
from django.shortcuts import render
from .models import Hiker, Hike
from .serializers import HikerSerializer, HikeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class HikersView(ListCreateAPIView):
    serializer_class = HikerSerializer
    queryset = Hiker.objects.all()

class HikerView(RetrieveUpdateDestroyAPIView):
    serializer_class = HikerSerializer
    queryset = Hiker.objects.all()
    lookup_field = 'id'

class HikesView(ListCreateAPIView):
    serializer_class = HikeSerializer
    queryset = Hike.objects.all()
    lookup_field = 'hiker_id'

class HikeView(RetrieveUpdateDestroyAPIView):
    serializer_class = HikeSerializer
    queryset = Hike.objects.all()
    lookup_field = 'id'
