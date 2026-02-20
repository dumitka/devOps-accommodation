from rest_framework.routers import DefaultRouter
from .views import AccommodationViewSet

router = DefaultRouter()
router.register(r'', AccommodationViewSet)

urlpatterns = router.urls