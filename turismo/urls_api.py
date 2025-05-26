from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TouristSpotViewSet, EventViewSet

router = DefaultRouter()
router.register(r'spots', TouristSpotViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]