from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user.html')


def project(request):
    return render(request, 'project.html')
