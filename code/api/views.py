from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from news_service.models import News
from weather_service.models import CityWeather
from spotify_service.models import SpotifyPlayer
from youtube_service.models import Youtube_subs, Youtube_views, Youtube_popular
from gorafi.models import Gorafi
from .serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CityWeatherViewSet(viewsets.ModelViewSet):
	queryset = CityWeather.objects.all()
	serializer_class = CityWeatherSerializer

class NewsViewSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer

class SpotifyPlayerViewSet(viewsets.ModelViewSet):
	queryset = SpotifyPlayer.objects.all()
	serializer_class = SpotifyPlayerSerializer

class YoutubeSubsViewSet(viewsets.ModelViewSet):
	queryset = Youtube_subs.objects.all()
	serializer_class = YoutubeSubsSerializer

class GorafiViewSet(viewsets.ModelViewSet):
	queryset = Gorafi.objects.all()
	serializer_class = GorafiSerializer

class Youtube_viewsViewSet(viewsets.ModelViewSet):
	queryset = Youtube_views.objects.all()
	serializer_class = Youtube_viewsSerializer

class Youtube_topViewSet(viewsets.ModelViewSet):
	queryset = Youtube_popular.objects.all()
	serializer_class = Youtube_popularSerializer