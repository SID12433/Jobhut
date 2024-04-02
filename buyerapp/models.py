from django.db import models
from django.conf import settings
# Create your models here.

class BuyerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="buyer_profile")
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to="images/profile",default='images/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username