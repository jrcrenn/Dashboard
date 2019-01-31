from django.db import models
from django.contrib.auth.models import User

import feedparser

# Create your models here.


class Gorafi(models.Model): 
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	onglet_to_display = models.IntegerField(default = 1)
	
	def get(self, instance):
		url = "http://www.legorafi.fr/feed/"
		feed = feedparser.parse(url)
		tab = []
		for elem in feed["items"]:
			tab.append({
			'name' : "Le Gorafi",
			'title' : elem['title'],
			'pic' : elem['custom_thumbnail'],
			'link' : elem['links'][0]["href"],
			})
		return {
			"tab" : tab,
			"id": instance.id,
		}

	def __str__(self):
		return  "It's a pac of " + str(self.onglet_to_display) + " from Le Gorafi"

	class Meta:
        	verbose_name_plural = 'Gorafi'