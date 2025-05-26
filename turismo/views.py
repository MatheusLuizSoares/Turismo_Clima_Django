from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from .models import TouristSpot, Event
from .serializers import TouristSpotSerializer, EventSerializer
from .utils import get_weather_data

# API Views
class TouristSpotViewSet(viewsets.ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Template Views
class HomeView(ListView):
    model = TouristSpot
    template_name = 'home.html'
    context_object_name = 'spots'
    ordering = ['-created_at']
    paginate_by = 9

class SpotDetailView(DetailView):
    model = TouristSpot
    template_name = 'spot_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spot = self.object
        
        context['weather'] = get_weather_data(spot.location) if spot.location else None
        context['events'] = Event.objects.filter(spot=spot).order_by('-date')
        
        return context