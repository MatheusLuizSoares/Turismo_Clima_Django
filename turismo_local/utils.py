import requests
from django.conf import settings

def get_weather_data(cidade):
    if not cidade:
        return None
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},BR&appid={settings.WEATHER_API_KEY}&units=metric&lang=pt"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'temp': round(data['main']['temp']),
                'description': data['weather'][0]['description'].capitalize(),
                'icon': f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                'humidity': data['main']['humidity'],
                'wind_speed': round(data['wind']['speed'] * 3.6, 1)
            }
        return None
    except Exception as e:
        print(f"Erro na API do clima: {e}")
        return None