from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccommodationViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'accommodations', AccommodationViewSet, basename='accommodation')
router.register(r'availabilities', AvailabilityViewSet, basename='availability')

urlpatterns = [
    path('', include(router.urls)),
]