from django.contrib import admin
from .models import TouristSpot


@admin.register(TouristSpot)
class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_location', 'opening_hours')
    
    def formatted_location(self, obj):
        try:
            cidade, pais = obj.location.split(',', 1)  # Split apenas na primeira vírgula
            return f"{cidade.strip()} • {pais.strip().upper()}"
        except ValueError:
            return f" Formato inválido: {obj.location}"
    
    formatted_location.short_description = 'Localização'
    formatted_location.admin_order_field = 'location'

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'description', 'image')
        }),
        ('Detalhes', {
            'fields': ('location', 'opening_hours'),
            'description': '''
                <div class="alert alert-info">
                    <strong>Formato requerido para localização:</strong><br>
                    "Cidade, País" (Ex: Natal, Brasil)
                </div>
            '''
        }),
    )