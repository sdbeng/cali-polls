from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Home- Django Project</h1>')