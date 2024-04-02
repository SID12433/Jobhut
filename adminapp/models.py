from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin","Admin"),
        ("coder", "Coder"),
        ("buyer", "Buyer"),
    ]
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default="coder")



class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to="images/profile",default='images/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username