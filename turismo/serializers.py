# serializers.py
from rest_framework import serializers
from .models import TouristSpot, Event

# tourism/serializers.py
class TouristSpotSerializer(serializers.ModelSerializer):
      image = serializers.ImageField(
        max_length=None, 
        use_url=True,  # Garante URL absoluta
        required=False)
      class Meta:
        model = TouristSpot
        fields = ['id', 'name', 'description', 'location', 'opening_hours', 'image', 'created_at']
   
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'