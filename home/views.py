from django.shortcuts import render
from django.config import settings 
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    try:
        restaurant_name = getattr(settings,"RESTAURANT_NAME","Our Restaurant")
        phone_number = getattr(settings,"RESTAURANT_PHONE","Not Available")
        location = RestaurantLocation.objects.first()
    except Exception as e:
        print(f"error loading restaunrant info {e}")
        return HttpResponseServerError("Something went wrong please try again later.")
    
    context = {
        "restaurant_name" : settings.RESTAURANT_NAME,
        "phone_number" : settings.RESTAURANT_PHONE,
        "location" : location
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = ContactForm()
        context={
            "restaurant_name" : settings.RESTAURANT_NAME,
            "phone_number" : settings.RESTAURANT_PHONE,
            "form" : form,
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

def contact(request):
    context = {
        "restaurant_name" = settings.RESTAURANT_NAME,
        "restaurant_phone" = settings.RESTAURANT_PHONE,
        "restaurant_email" = settings.RESTAURANT_EMAIL,
        "restaurant_address" = settings.RESTAURANT_ADDRESS,
    }
    return render(request, "contact.html", context)

def reservation(request):
    context {
        "restaurant_name" = settings.RESTAURANT_NAME,
    }
    return render(request, 'reservation.html' ,context)
    
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/feedback_thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'home.feedback.html',{'form': form})        