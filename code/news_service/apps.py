from django.apps import AppConfig

from .form import NewsForm
from .models import News
from api.views import NewsViewSet
from api.serializers import NewsSerializer

class NewsServiceConfig(AppConfig):
	name = 'News'

	about = {
        	"name": name,
        	"widgets": [{
			"name": "Last news",
        	    	"description": "Show the news" ,
        	    	"params": [{
				"name": "topic" ,
				"type": "string"
			}],
		}]
	}

	widgets = [{
		"name": about["widgets"][0]["name"],
		"template_name": "news_service.html",
		"model": News,
		"form": NewsForm,
		"api": {
			"api_route": "news",
			"api_url": "/api/news",
			"ViewSet": NewsViewSet,
			"Serializer": NewsSerializer
		}
	}]
    
