from django.apps import AppConfig

from .form import CityWeatherForm
from .models import CityWeather
from api.views import CityWeatherViewSet
from api.serializers import CityWeatherSerializer
class WeatherServiceConfig(AppConfig):
	name = 'Weather'

	about = {
        	"name": name,
        	"widgets": [{
			"name": "City Weather" ,
        	    	"description": "Show the city's weather" ,
        	    	"params": [{
				"name": "city" ,
				"type": "string"
			}],
		}]
	}

	widgets = [{
		"name": name,
		"template_name": "Weather.html",
		"model": CityWeather,
		"form": CityWeatherForm,
		"api": {
			"api_route": "city_weather",
			"api_url": "/api/city_weather",
			"ViewSet": CityWeatherViewSet,
			"Serializer": CityWeatherSerializer
		}
	}]