from django.shortcuts import render
from .models import Hiker
from .serializers import HikerSerializer
from rest_framework.generics import CreateAPIView

class HikerCreateView(CreateAPIView):
    serializer_class = HikerSerializer
    queryset = Hiker.objects.all()