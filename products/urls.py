from django.urls import path
from . import views

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/', views.menu , name="menu"),
]