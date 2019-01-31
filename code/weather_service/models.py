from django.db import models
from django.contrib.auth.models import User

import requests
# Create your models here.

class CityWeather(models.Model):
	city = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get(self, instance):
		city = self.city
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=580ee204e0c4a86011a0e985d2a01091'
		city_weather = requests.get(url.format(city)).json()
		return {
        		'city' : city,
        		'temperature' : city_weather['main']['temp'],
        		'description' : city_weather['weather'][0]['description'],
        		'icon' : city_weather['weather'][0]['icon']
        	}

	def __str__(self):
		return "Weather of " + self.city
	class Meta:
        	verbose_name_plural = 'Cities weather'