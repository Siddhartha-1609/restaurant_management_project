from django.urls import path
from . import views
from .views import MenuView
urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('api/menu/', MenuView.as_view() , name="menu-api"),
]