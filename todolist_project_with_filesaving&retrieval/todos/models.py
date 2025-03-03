from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Background Image - {self.id}"
