from django.shortcuts import render
from django.config import settings 
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    context = {
        "restaurant_name" : settings.RESTAURANT_NAME,
        "phone_number" : settings.RESTAURANT_PHONE
    }
    return render(request,'home.html',context)

def about(request):
    context = {
        "restaurant_name" : settings.RESTAURANT_NAME,
        "description" : (
            "Family-owned restaurant serving fresh, locally sourced food."
            "We focus on warm hospitality and seasonal menus"
        ),
        "image_url" : "https//:images.pexels.com/photos/11236793/pexels-photo-11236793.jpg",
    }
    return render(request, 'about.html' , context)

def contacr(request):
    context = {
        "restaurant_name" = settings.RESTAURANT_NAME,
        "restaurant_phone" = settings.RESTAURANT_PHONE,
        "restaurant_email" = settings.RESTAURANT_EMAIL,
        "restaurant_address" = settings.RESTAURANT_ADDRESS,
    }
    return render(request, "contact.html", context)
    