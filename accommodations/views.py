from rest_framework import viewsets
from .models import Accommodation, Availability
from .serializers import AccommodationSerializer, AvailabilitySerializer


class AccommodationViewSet(viewsets.ModelViewSet):
    serializer_class = AccommodationSerializer

    def get_queryset(self):
        queryset = Accommodation.objects.all()
        host_id = self.request.query_params.get('host_id')
        if host_id:
            queryset = queryset.filter(host_id=host_id)
        return queryset


class AvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        queryset = Availability.objects.all()
        acc_id = self.request.query_params.get('accommodation_id')
        if acc_id:
            queryset = queryset.filter(accommodation_id=acc_id)
        return queryset
