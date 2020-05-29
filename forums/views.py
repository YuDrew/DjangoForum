from django.shortcuts import render
from django.http import HttpResponse

#Variables

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



# Create your views here.

def index(request):
    return HttpResponse('Hello, world. You\'re at the forums index.')

def home(request):
    context = {
        'posts': posts
	}
    return render(request, 'forums/home.html', context)


def about(request):
    return render(request, 'forums/about.html', {'title': 'About'})