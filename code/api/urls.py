from django.contrib import admin
from rest_framework import routers
from api.views import CityWeatherViewSet, UserViewSet
from django.urls import path, include

from weather_service.apps import WeatherServiceConfig
from news_service.apps import NewsServiceConfig
from youtube_service.apps import YoutubeServiceConfig

from gorafi.apps import GorafiServiceConfig


router = routers.DefaultRouter()

for service in [
	WeatherServiceConfig,
	NewsServiceConfig,
	YoutubeServiceConfig,
	GorafiServiceConfig,
	]:
	for widget in service.widgets:
		router.register(widget["api"]["api_route"], widget["api"]["ViewSet"])
router.register('users', UserViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]