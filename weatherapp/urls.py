from django.contrib import admin
from django.urls import path, include
from weatherapp.views import WeatherAPIView

urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather'),
]