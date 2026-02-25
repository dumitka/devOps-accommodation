from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Accommodation

class AccommodationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        User = get_user_model()
        self.user = User.objects.create_user(
            username="test",
            password="testpass"
        )

        self.client.force_authenticate(user=self.user)

    def test_create_accommodation(self):
        data = {
            "host_id": 1,
            "title": "Test Apartment",
            "description": "Nice place",
            "location": {"city": "Novi Sad"},
            "price_per_night": "50.00",
            "guests": 2,
            "amenities": {"wifi": True}
        }

        response = self.client.post("/api/accommodations/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Accommodation.objects.count(), 1)