from django.shortcuts import render
from django.config import settings 
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
#taken from model

def homepage(request):

    cart = request.session.get("cart",{})
    cart_count = sum(cart.values)
    restaurant = Restaurant.objects.first()
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=quer)
    else:
        menu_items = MenuItem.objects.all()
    try:
        restaurant_name = getattr(settings,"RESTAURANT_NAME","Our Restaurant")
        phone_number = getattr(settings,"RESTAURANT_PHONE","Not Available")
        location = RestaurantLocation.objects.first()
    except Exception as e:
        print(f"error loading restaunrant info {e}")
        return HttpResponseServerError("Something went wrong please try again later.")
    current_time = timezone.now()
    context = {
        "restaurant_name" : settings.RESTAURANT_NAME,
        "phone_number" : restaurant.phone_number if restaurant else "not available",
        "location" : location,
        "cart_count" : cart_count,
        "logo" : restaurant.logo.ur if restaurant and restaurant_logo else None,
        "current_time" : current_time,
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
            "query" : query
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

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            subject = f"new contact form submission from {contact.name}"
            message = f"""
            you have a new contact form submission
            name : {contact.name}
            email : {contact.email}
            message : {contact.message}
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.RESTAURANT_EMAIL],
                fail_silently = False
            )
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request,"contact.html",context)

def add_to_cart(request, item_id):
    cart = request.session.get("cart",{})
    cart[str(item_id)] = cart.get(str(item_id),0)+1
    request.session["cart"] = cart
    return redirect("homepage")

def faq(request):
    faqs = [
        {"question":"What are your opening hours?",
         "answer":"We are daily open from 10:00 AM to 10:00 PM."},
        {"question":"Do you offer home delivery?",
         "answer" : "Yes, we provide delivery within 5km radius."},
        {"question": "Can I reserve a table?",
         "answer" : "Absolutely! Call us at the number listed on our homepage to reserve a table"},
        {"question": "Do you have vegetarian options?",
         "answer" : "Yes, we have a wide  variety of vegetarian dishes available"},
    ]
    return render(request, "faqs.html",{"faqs": faqs})