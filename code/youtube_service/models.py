from django.db import models
from django.contrib.auth.models import User
import urllib
import json
# Create your models here.

key = 'AIzaSyCC_5hS2vAiALrdUs7pZVk9QY8MAjREKLA'
class Youtube_subs(models.Model):
	channel = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get(self, instance):
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + self.channel + "&key=" + key).read()
		if len(json.loads(data)["items"]) == 0:
			return {'error': "Can't find " + self.channel + "'s channel"}
		subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername=" + self.channel + "&key=" + key).read()
		pic = json.loads(data)["items"][0]["snippet"]["thumbnails"]["default"]
		return {
			'subs': subs,
			'channel': instance.channel,
			'pic': pic,
		}

	def __str__(self):
		return "Subs of " + self.channel
	class Meta:
        	verbose_name_plural = 'Channels subs'

class Youtube_views(models.Model):
	video = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def get(self, instance):
		data = json.loads(urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + self.video + "&key=" + key).read())
		if len(data["items"]) == 0:
			return {'error': "Can't find video with video_id " + self.video}
		return {
			'views': data["items"][0]["statistics"]["viewCount"],
			'likes': data["items"][0]["statistics"]["likeCount"],
			'dislikes': data["items"][0]["statistics"]["dislikeCount"],
			'comments': data["items"][0]["statistics"]["commentCount"],
			'video': instance.video
		}

	def __str__(self):
		return "Subs of " + self.video
	class Meta:
        	verbose_name_plural = 'Videos view'

class Youtube_popular(models.Model):
	nb = models.IntegerField(default=5)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)

	def get(self, instance):
		videos = []
		try:
			data = json.loads(urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=contentDetails&chart=mostPopular&regionCode=FR&maxResults="+ str(instance.nb) +"&key=" + key).read())
		except urllib.error.HTTPError:
			return {'error': "Error loading"}
		if len(data["items"]) == 0:
			return {'error': "Error loading"}
		return {
			"videos": {
				"id": [video["id"] for video in data["items"]]
			}
		}

	def __str__(self):
		return str(self.nb) + " popular videos"
	class Meta:
        	verbose_name_plural = 'Best Videos'
