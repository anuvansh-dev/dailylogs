from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = [('Voting Open', 'Voting Open'), ('Active', 'Active'), 
                      ('Discarded', 'Discarded'), ('Completed', 'Completed')]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Voting Open')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'project') # Ensures a user votes only once per project
        
    
class FacilityRequest(models.Model):
    CATEGORY_CHOICES = [('Roads', 'Roads'), ('Water Supply', 'Water Supply'), 
                        ('Electricity', 'Electricity'), ('Parks', 'Parks'), ('Cleaning', 'Cleaning'), 
                        ('Other', 'Other')]
    
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), 
                      ('Rejected', 'Rejected'), ('Completed', 'Completed')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    image = models.ImageField(upload_to='facility_request_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.category} ({self.status})"
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    facility_request = models.ForeignKey(FacilityRequest, null=True, blank=True, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.project:
            return f"Feedback for Project: {self.project.name} by ({self.user.username} - {self.rating})"
        elif self.facility_request:
            return f"Feedback for Facility Request: {self.facility_request} by ({self.user.username} - {self.rating})"
        else:
            return f"Feedback by {self.user.username}"
        
        
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility_request = models.ForeignKey(FacilityRequest, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Notification for {self.user.username} - {self.message}"