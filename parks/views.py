from hikers import serializers
from .models import Park, Trail
from .serializers import ParkListSerializer, ParkDetailSerializer, ParkNameSerializer, TrailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ParkListView(ListAPIView):
    serializer_class = ParkListSerializer
    queryset = Park.objects.all()

class ParkDetailView(RetrieveAPIView):
    serializer_class = ParkDetailSerializer
    queryset = Park.objects.all()
    lookup_field = 'slug'

@api_view(['GET'])
def map_view(request, slug, *args, **kwargs):
    data = {
        'slug': slug
    }
    status = 200
    try:
        park = Park.objects.get(slug=slug)
        data['map'] = park.trail_map
    except:
        data['message'] = 'Not found'
        status = 404
    return Response(data, status=status)

class TrailListView(ListAPIView):
    serializer_class = TrailSerializer
    
    def get_queryset(self):
        park_id = self.kwargs['park_id']
        return Trail.objects.filter(park_id=park_id)

class ParkNameView(ListAPIView):
    serializer_class = ParkNameSerializer
    queryset = Park.objects.all()