from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator



class Coder(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    aadharimg=models.ImageField(upload_to="images",null=True)
    aadharno=models.PositiveIntegerField()
    usertype=models.CharField(max_length=100,default='coder')
    
