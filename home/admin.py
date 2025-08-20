from django.contrib import admin
from .models import RestaurantLocation

# Register your models here.
admin.site.register(Feedback)

class RestaurantLocationAdmin(admin.ModelAdmin):
    list_display = ("address","city","state","zip_code")