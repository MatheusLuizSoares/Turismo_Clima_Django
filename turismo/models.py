from django.db import models


# tourism/models.py
from django.core.validators import RegexValidator



class TouristSpot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZÀ-ú\s]+,\s*[A-Za-z]{2,}$',
                message='Formato requerido: "Cidade, País" (Ex: Natal, Brasil)',
                code='invalid_location'
            )
        ],
        
    )
    opening_hours = models.CharField(
        max_length=50,
        validators=[RegexValidator(r'^\d{2}:\d{2} às \d{2}:\d{2}$', 'Formato: 08:00 às 18:00')])
    image = models.ImageField(upload_to='spots/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} at {self.spot.name}"