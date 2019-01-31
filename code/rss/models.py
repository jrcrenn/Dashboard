from django.db import models

from django.contrib.auth.models import User

import feedparser

# Create your models here.

class Rss(models.Model):
	flux = models.CharField(max_length = 128)
	onglet_to_display = models.IntegerField(default = 1)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def get(self, instance):
		feed = feedparser.parse(self.flux)		
		tab = []
		try:
			for elem in feed["items"]:
				tab.append({
				'name' : feed["title"],
				'title' : elem['title'],
				'pic' : elem['enclosure']['url'],
				'link' : elem['link'],
				})
			return {
				"tab" : tab,
				"id": instance.id,
			}
		except ValueError:
			 return {
				"tab" : None,
				"id": instance.id,
			}
		

	def __str__(self):
		return "An RSS flux from " + self.flux + "with " + self.onglet_to_display + " onglets"

	class Meta:
        	verbose_name_plural = 'RSS Flux'