from rest_framework import serializers
from .models import Accommodation, Availability

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class AccommodationSerializer(serializers.ModelSerializer):
    availabilities = AvailabilitySerializer(many=True, read_only=True)

    class Meta:
        model = Accommodation
        fields = '__all__'