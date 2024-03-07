from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Hello! It's my project")

def current_date(request):
    now = datetime.now()
    return HttpResponse("Current date and time: {}".format(now))

def goodby(request):
    return HttpResponse("Goodbye user!")