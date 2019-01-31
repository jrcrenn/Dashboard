from django.apps import AppConfig

from .models import SpotifyPlayer
from .form import SpotifyPlayerForm
from api.views import SpotifyPlayerViewSet
from api.serializers import SpotifyPlayerSerializer

class SpotifyServiceConfig(AppConfig):
	name = 'Spotify'

	about = {
        	"name": name,
        	"widgets": [{
			    "name": "SpotifyPlayer" ,
        	    	"description": "Listen music on dashboard" ,
        	    	"params": [{
				        "name": "Playlist/Album url",
				        "type": "string"
			}],
		}]
	}

	widgets = [{
		"name": about["widgets"][0]["name"],
		"template_name": "SpotifyPlayer.html",
		"model": SpotifyPlayer,
		"form": SpotifyPlayerForm,
		"api": {
			"api_route": "city_weather",
			"api_url": "/api/city_weather",
			"ViewSet": SpotifyPlayerViewSet,
			"Serializer": SpotifyPlayerSerializer
		}
	}]