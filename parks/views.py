from .models import Park
from .serializers import ParkSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ParkListView(ListAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.all()

class ParkDetailView(RetrieveAPIView):
    serializer_class = ParkSerializer
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