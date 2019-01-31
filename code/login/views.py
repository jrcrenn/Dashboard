from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

class SignUp(View):
	def get(self, request):
		form = UserCreationForm()
		return render(request, 'signup/signup.html', {'form': form})
	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
            		form.save()
            		username = form.cleaned_data.get('username')
            		raw_password = form.cleaned_data.get('password1')
            		user = authenticate(username=username, password=raw_password)
            		login(request, user)
            		return redirect('signin')
		return redirect('signup')
	

class SignIn(View):
	def get(self, request):
		return render(request, 'signin/signin.html')
	
	def post(self, request):
		username = request.POST.get('username', False)
		password = request.POST.get('password', False)
		if username is not None and password is not None:
			user = authenticate(username=username, password=password)
			if user is not None and user.is_active:
				login(request, user)
				return redirect('home')
		return redirect('signin')

@login_required
def logoutView(request):
	logout(request)
	return redirect('home')