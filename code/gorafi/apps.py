from django.apps import AppConfig



from .form import GorafiForm
from .models import Gorafi
from api.views import GorafiViewSet
from api.serializers import GorafiSerializer

class GorafiServiceConfig(AppConfig):
    name = 'Gorafi'

    about = {
        	"name": name,
        	"widgets": [{
			"name": "Le Gorafi" ,
        	    	"description": "Show the Le Gorafi" ,
        	    	"params": [{
				"name": "topic" ,
				"type": "string"
			}],
		}]
	}

    widgets = [{
		"name": about["widgets"][0]["name"],
		"template_name": "gorafi.html",
		"model": Gorafi,
		"form": GorafiForm,
		"api": {
			"api_route": "Gorafi",
			"api_url": "/api/Gorafi",
			"ViewSet": GorafiViewSet,
			"Serializer": GorafiSerializer
		}
	}]
    