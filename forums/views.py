from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import NewUserForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone
from django.views.generic import ListView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# General Site Views
def about(request):
    return render(request, 'forums/about.html', {'title': 'About'})

# Post Viewing Views
@login_required()
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'forums/home.html', context= context)

@login_required()
def account(request):
	context = {
		'posts': Post.objects.filter(author=request.user)
	}
	return render(request, 'forums/account.html', context= context)

@method_decorator(login_required, name='dispatch')
class user_posts(ListView):
	model = Post
	template_name = 'forums/user_posts.html'
	context_object_name = 'posts'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

# Creating and Deleting Views
@login_required
def create_post(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			print(type(post))
			post.author = request.user
			print(len(request.FILES.keys()))
			if 'image' in request.FILES.keys():
				post.image = request.FILES['image']
			else: 
				print("WHAT")
			post.save()
			return redirect('forums:home')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(request, 'forums/create_post.html', context={'form':form})
	
	form = PostForm()
	return render(request, 'forums/create_post.html', context={'form':form})

@method_decorator(login_required, name='dispatch')
class delete_post(DeleteView):
	model = Post
	success_url = '/account/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

# Auth Views
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