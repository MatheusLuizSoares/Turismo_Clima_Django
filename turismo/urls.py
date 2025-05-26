from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TouristSpotViewSet,
    EventViewSet,
    HomeView,
    SpotDetailView
)

router = DefaultRouter()
router.register(r'spots', TouristSpotViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    # API Endpoints
    path('api/', include(router.urls)),
    
    # Template Views
    path('', HomeView.as_view(), name='home'),
    path('spot/<int:pk>/', SpotDetailView.as_view(), name='spot_detail'),
]