from django.db import models
from django.conf import settings
# Create your models here.

class CoderProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="coder_profile")
    phone = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    skills = models.TextField()
    experience = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ("approved", "Approved"),
        ("pending", "Pending"),
    ]
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="pending")
    SPECIALIZATION_CHOICES = [
        ("front_end", "Front End"),
        ("back_end", "Back End"),
        ("full_stack", "Full Stack"),
    ]
    specialized_in = models.CharField(max_length=200, choices=SPECIALIZATION_CHOICES)
    bio = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to="images/",default='images/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
