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
        fields = [
            'id', 'host_id', 'title', 'description', 'location', 
            'price_per_night', 'price_per_guest', 'min_guests', 
            'max_guests', 'automatic_approval', 'amenities', 'images', 'availabilities'
        ]
