from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SpotifyPlayer(models.Model):
	title =  models.CharField(max_length=30)
	url = models.CharField(max_length=300)
	width = models.IntegerField(default='300')
	height = models.IntegerField(default='380')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get(self, instance):
		url = ""
		if self.url.find("spotify:") >= 0:
			url = self.url.split(':')[1:]
			url = '/'.join(url)
		elif self.url.find("https://open.spotify.com/") >= 0:
			print(self.url)
			url = "https://open.spotify.com/embed/" + self.url.replace('https://open.spotify.com/', '')
			print(url)
		return {
			'url': url
		}

	def __str__(self):
		return "SpotifyPlayer " + self.title
	class Meta:
		verbose_name_plural = "Spotify players"