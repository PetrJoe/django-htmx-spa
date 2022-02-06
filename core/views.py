from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import *

def home(request):
    return render(request, 'home.html')

def landingpage(request):
    return render(request, 'landingpage.html')


def about(request):
	todos = Todo.objects.all()
	context = {
        'todos': todos
	}
	return render(request, 'pages/about.html', context)