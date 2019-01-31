from django.apps import AppConfig

from .models import Youtube_subs, Youtube_views, Youtube_popular
from .form import Youtube_subsForm, Youtube_viewsForm, Youtube_popularForm

from api.views import YoutubeSubsViewSet, Youtube_viewsViewSet
from api.serializers import YoutubeSubsSerializer

class YoutubeServiceConfig(AppConfig):
    name = 'Youtube'

    about = {
        	"name": name,
        	"widgets": [{
			"name": "Youtube_subs" ,
        	    	"description": "Count subs of a channel" ,
        	    	"params": [{
				        "name": "channel_name",
				        "type": "string"
			}],
		}, {
			"name": "Video Player",
        	    	"description": "Stats about a video",
        	    	"params": [{
				        "name": "video id",
				        "type": "string"
			}],
		}, {
			"name": "Most popular videos",
        	    	"description": "List all most popular videoss",
        	    	"params": [{
				        "name": "Number of videos",
				        "type": "integrer"
			}],
		}]
	}

    widgets = [{
		"name": about["widgets"][0]["name"],
		"model": Youtube_subs,
		"form": Youtube_subsForm,
		"template_name": "Youtube_subs.html",
		"api": {
			"api_route": "youtube_subs",
			"api_url": "/api/youtube_subs",
			"ViewSet": YoutubeSubsViewSet,
			"Serializer": YoutubeSubsSerializer
		}
	}, {
		"name": about["widgets"][1]["name"],
		"model": Youtube_views,
		"form": Youtube_viewsForm,
		"template_name": "Youtube_views.html",
		"api": {
			"api_route": "youtube_views",
			"api_url": "/api/youtube_views",
			"ViewSet": YoutubeSubsViewSet,
			"Serializer": YoutubeSubsSerializer
		}
	}, {
		"name": about["widgets"][2]["name"],
		"model": Youtube_popular,
		"form": Youtube_popularForm,
		"template_name": "Youtube_top.html",
		"api": {
			"api_route": "youtube_top",
			"api_url": "/api/youtube_top",
			"ViewSet": YoutubeSubsViewSet,
			"Serializer": YoutubeSubsSerializer
		}
	}]