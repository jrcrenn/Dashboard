from django.forms import ModelForm, TextInput

from .models import CityWeather

class CityWeatherForm(ModelForm):
	class Meta:
		model = CityWeather
		exclude = ['user']
		widgets = {
			'city': TextInput(attrs={'class': ' form-control'}),
        	}