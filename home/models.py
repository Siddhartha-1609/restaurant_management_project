from django.db import models

# Create your models here.
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