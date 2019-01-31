from django.forms import ModelForm, TextInput

from .models import Gorafi

class GorafiForm(ModelForm):
	class Meta:
		model = Gorafi
		exclude = ['user']