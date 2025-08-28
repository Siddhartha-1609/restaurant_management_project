from django.db import models

# Create your models here.
#feedback
class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address},{self.city},{self.state},{self.zip_code}" 
#phone number from model
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    logo = models.ImageField(upload_to ="restaurant_logos/",blank=True,null=True)
    

    def __str__(self):
        return self.name

class Special(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
