from django.forms import ModelForm, TextInput

from .models import SpotifyPlayer

class SpotifyPlayerForm(ModelForm):
	class Meta:
		model = SpotifyPlayer
		exclude = ['user']
		widgets = {
			'url': TextInput(attrs={'class': ' form-control'}),
        	}