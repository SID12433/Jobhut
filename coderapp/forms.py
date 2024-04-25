from django import forms
from django.contrib.auth.forms import UserCreationForm
from adminapp.models import *

class RegistrationForm(UserCreationForm):
   GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

   gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;'}))

   class Meta:
      model=Coder
      fields=["name","phone","email_address","address","designation","gender","skills","profile","aadhar_image","aadhar_no","pan_image","pan_no","status","username"]
      widgets={
         'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Name'}),
         'phone': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Phone'}),
         'email_address': forms.EmailInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Email Address'}),
         'address': forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Address', 'rows': 3}),
         'designation': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'designation'}),
         'skills': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'skills'}),
         'aadhar_no': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Aadhar no'}),
         'pan_no': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'pan no'}),
         'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Username'}),
         
         
      }

   def  __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
         field.help_text = None

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)         

class CollaboratorForm(forms.ModelForm):
   class Meta:
      model=Collaborate
      fields=["note","file"]   
      
      
class AddBidForm(forms.ModelForm):
   class Meta:
      model=Bid
      fields=["bid_amount","note"]  


class AddWorkForm(forms.ModelForm):
   class Meta:
      model=BidDetails
      fields=["doc"]  
      
      
class ProfileUpdateForm(forms.ModelForm):
   class Meta:
      model=Coder
      fields=["phone","address","bio","profile","skills"]