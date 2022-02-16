from cgitb import lookup
from django.shortcuts import render
from .models import Hiker, Hike
from .serializers import HikerSerializer, HikeSerializer, TrailsByParkHikerSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class HikersView(ListCreateAPIView):
    serializer_class = HikerSerializer
    queryset = Hiker.objects.all()

class HikerView(RetrieveUpdateDestroyAPIView):
    serializer_class = HikerSerializer
    queryset = Hiker.objects.all()
    lookup_field = 'id'

class HikesView(ListCreateAPIView):
    serializer_class = HikeSerializer

    def get_queryset(self):
        hiker_id = self.kwargs['hiker_id']
        return Hike.objects.filter(hiker_id=hiker_id)

class HikeView(RetrieveUpdateDestroyAPIView):
    serializer_class = HikeSerializer

    def get_queryset(self):
        hiker_id = self.kwargs['hiker_id']
        id = self.kwargs['id']
        return Hike.objects.filter(hiker_id=hiker_id, id=id)

class TrailsByParkHikerView(ListAPIView):
    serializer_class = TrailsByParkHikerSerializer

    def get_queryset(self):
        park_id = self.kwargs['park_id']
        hiker_id = self.kwargs['hiker_id']
        return Hike.objects.filter(park_id=park_id, hiker_id=hiker_id)