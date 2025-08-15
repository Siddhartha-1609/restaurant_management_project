from django.db import models

# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(max_lenght = 100)
    email = models.EmailField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"