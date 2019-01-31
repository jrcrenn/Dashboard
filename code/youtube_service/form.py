from django.forms import ModelForm, TextInput

from .models import Youtube_subs, Youtube_views, Youtube_popular

class Youtube_subsForm(ModelForm):
	class Meta:
		model = Youtube_subs
		exclude = ['user']
		widgets = {
			'channel': TextInput(attrs={'class': ' form-control'}),
        	}

class Youtube_viewsForm(ModelForm):
	class Meta:
		model = Youtube_views
		exclude = ['user']
		widgets = {
			'channel': TextInput(attrs={'class': ' form-control'}),
        	}
		labels = {
            		'video': 'Video ID',
        	}

class Youtube_popularForm(ModelForm):
	class Meta:
		model = Youtube_popular
		exclude = ['user']
		widgets = {
			'nb': TextInput(attrs={'class': ' form-control'}),
        	}
		labels = {
            		'nb': 'Number of videos',
        	}