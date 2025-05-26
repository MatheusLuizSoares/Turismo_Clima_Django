import requests
from django.conf import settings

def get_weather_data(location):
    if not location:
        return None
    
    try:
        # Formatação automática para "Cidade,País"
        if ',' not in location:
            location = f"{location.strip()},BR"  # Assume Brasil como padrão
            
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={settings.WEATHER_API_KEY}&units=metric&lang=pt"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'temp': round(data['main']['temp']),
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': round(data['wind']['speed'] * 3.6, 1)  # Converte m/s para km/h
            }
        return None
    except Exception as e:
        print(f"Erro na API do clima: {e}")
        return None