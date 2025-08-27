from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage, name = 'homepage'),
    path('about/',views.about , name = "about"),
    path('contact/',views.contact, name = "contact"),
    path('reservation/',views.reservation, name = "reservation"),
    path('feedback/',views.feedback_view, name = "feedback"),
    path('faqs/',views.faqs , name= "FAQ's"),
    path("login/",auth_views.LoginView.as_view(template_name="home.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page="homepage"),name="logout"),
]