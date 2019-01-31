from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from spotify_service.apps import SpotifyServiceConfig
from weather_service.apps import WeatherServiceConfig
from news_service.apps import NewsServiceConfig
from youtube_service.apps import YoutubeServiceConfig
from gorafi.apps import GorafiServiceConfig

services = [
	WeatherServiceConfig,
	SpotifyServiceConfig,
	NewsServiceConfig,
	YoutubeServiceConfig,
	GorafiServiceConfig,
	]
	
class Index(View):
	def get(self, request):
		widgets = []
		for service in services:
			for widget in service.widgets:
				for w in widget["model"].objects.filter(user=request.user):
					widgets.append({
						"template": "widgets/" + widget["template_name"],
						"template_name": widget["template_name"],
						"data": w.get(w),
					})
		print(widgets)
		return render(request, 'index.html', {
			'widgets': widgets,
		})
	def post(self, request):
		pass
class AddWidget(View):
	def get(self, request):
		forms = []
		for service in services:
			w = []
			for widget in service.widgets:
				w.append({
					'name': widget["name"],
					'form': widget["form"]()
					})
			forms.append({
				"service": service.name,
				"widgets": w
			})
		return render(request, 'addWidget.html', {
			'forms': forms
		})
	
	def post(self, request):
		if request.POST["widget_name"] is None:
			return redirect('addWidget')
		for widgets in services:
			for widget in widgets.widgets:
				if widget["name"] == request.POST["widget_name"]:
					form = widget["form"](request.POST)
					print(widget["form"])
					print(form)
					if form.is_valid():
						f = form.save(commit=False)
						f.user = request.user
						f.save()
						return redirect('home')
		return redirect('addWidget')

class Settings(View):
	def get(self, request):
		forms = []
		for service in services:
			for widget in service.widgets:
				for w in widget["model"].objects.filter(user=request.user):
					forms.append({
						'name': widget["name"],
						'form': widget["form"](instance=w),
						'object': w
					})
		print(forms)
		return render(request, 'settings.html', {
			'forms': forms,
		})

	def post(self, request):
		if request.POST["widget_name"] is None:
			print("Can't found widget_name")
			return redirect('settings')
		for widgets in services:
			for widget in widgets.widgets:
				if widget["name"] == request.POST["widget_name"]:
					obj = widget["model"].objects.get(pk=request.POST["id"])
					if request.POST.get('delete'):
						obj.delete()
						return redirect('home')
					form = widget["form"](request.POST, instance=obj)
					if form.is_valid():
						f = form.save(commit=False)
						f.user = request.user
						f.save()
						return redirect('home')
		return redirect('settings')