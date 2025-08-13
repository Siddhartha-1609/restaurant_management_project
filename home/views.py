from django.shortcuts import render
from django.config import settings 
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse(f"Welcome to {settings.RESTAURANT_NAME}")