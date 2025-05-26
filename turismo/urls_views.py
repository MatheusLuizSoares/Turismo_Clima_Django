from django.urls import path
from .views import HomeView, SpotDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('spot/<int:pk>/', SpotDetailView.as_view(), name='spot_detail'),
]