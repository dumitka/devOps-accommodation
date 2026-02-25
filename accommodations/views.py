from rest_framework import viewsets
from .models import Accommodation
from .serializers import AccommodationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]