import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import json

class WeatherAPIView(APIView):
    def get(self, request):
        city = request.GET.get('city')
        if not city:
            return Response({'error': 'City parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        api_key = settings.OPENWEATHER_API_KEY
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)

        if response.status_code != 200:
            return Response({'error': 'City not found or invalid request.'}, status=response.status_code)

        data = response.json()

        for item in data.items():
            print(item)

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "country": data['sys']["country"]
        }

        return Response(weather_data)
