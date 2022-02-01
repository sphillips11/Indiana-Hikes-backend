from .models import Park
from .serializers import ParkSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ParkListView(ListAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.all()


class ParkDetailView(RetrieveAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.all()
    lookup_field = 'slug'