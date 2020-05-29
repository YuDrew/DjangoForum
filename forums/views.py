from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

#Dummy Posts

posts = [
	{
		'author': 'TestPerson',
		'title': "Forum Post 1",
		'content': "Wow it's the first post",
		'date_posted': 'May 31, 2020'
	},
	{
		'author': 'TestPerson',
		'title': "Forum Post 1",
		'content': "Wow it's the first post",
		'date_posted': 'May 31, 2020'
	}
]

def index(request):
    return HttpResponse('Hello, world. You\'re at the forums index.')

@login_required()
def home(request):
    context = {
        'posts': posts
	}
    return render(request, 'forums/home.html', context)

@login_required()
def account(request):
    return render(request, 'forums/account.html', {'title': 'Account'})

def about(request):
    return render(request, 'forums/about.html', {'title': 'About'})


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect('forums:home')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(request, 'forums/register.html', context={'form':form})
	form = NewUserForm
	return render(request, 'forums/register.html', context={'form':form})

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('forums:home')
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Unknown error. Form invalid.")
	form = AuthenticationForm()
	return render(request = request, template_name = 'forums/login.html', context = {'form': form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect('forums:home')