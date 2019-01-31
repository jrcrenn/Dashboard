import time
import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from weather_service.apps import WeatherServiceConfig
from gorafi.apps import GorafiServiceConfig
from news_service.apps import NewsServiceConfig
from spotify_service.apps import SpotifyServiceConfig
from weather_service.apps import WeatherServiceConfig
from youtube_service.apps import YoutubeServiceConfig

services = [
	WeatherServiceConfig,
	GorafiServiceConfig,
	NewsServiceConfig,
	SpotifyServiceConfig,
	WeatherServiceConfig,
	YoutubeServiceConfig,
]

class About(View):
	def get(self, request):
		return JsonResponse({
			"client": {
				"host": self.get_client_ip(request)
			},
			"server": {
				"current_time": int(time.time()),
				"services": [x.about for x in services]
			}
		})
	def get_client_ip(self, request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
        		ip = request.META.get('REMOTE_ADDR')
		return ip