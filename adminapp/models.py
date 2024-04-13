from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin","Admin"),
        ("coder", "Coder"),
        ("buyer", "Buyer"),
    ]
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default="coder")
    
    
class Buyer(User):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email_address = models.EmailField()
    address = models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    
    
class Skills(models.Model):
    no=models.PositiveIntegerField()
    skill=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    
    
class Coder(User):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email_address = models.EmailField()
    address = models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    proof = models.FileField(null=True, upload_to="images")
    profile = models.ImageField(upload_to="images", null=True)
    bio=models.CharField(max_length=100,null=True)
    status= models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    skills_required=models.CharField(max_length=100)
    budget=models.PositiveIntegerField()
    category=models.CharField(max_length=100)
    tags=models.CharField(max_length=100)
    deadline=models.CharField(max_length=100)
    status= models.BooleanField(default=True)


class Bid(models.Model):
    coder=models.ForeignKey(Coder,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    bid_amount=models.PositiveIntegerField()
    note=models.CharField(max_length=100,null=True)
    bid_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    CHOICES = [
        ("Pending","Pending"),
        ("On progress", "On progress"),
        ("Completed", "Completed"),
    ]
    progress=models.CharField(max_length=100,choices=CHOICES,default="Pending")
    
    
class BidDetails(models.Model):
    coder=models.ForeignKey(Coder,on_delete=models.CASCADE)
    doc=models.FileField(upload_to="files")
    bid=models.ForeignKey(Bid,on_delete=models.CASCADE)

    
    
class Payment(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    coder=models.ForeignKey(Coder,on_delete=models.CASCADE)
    bid=models.OneToOneField(Bid,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    payment_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    
class Collaborate(models.Model):
    note = models.CharField(max_length=100,)
    file= models.FileField(upload_to="files",null=True)
    coder = models.ForeignKey(Coder, on_delete=models.CASCADE)