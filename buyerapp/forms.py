from django import forms
from  adminapp.models import *
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model=Buyer
        fields=["name","address","companyname","country","phone","email_address","aadhar_image","aadhar_no","pan_image","pan_no","username","password1","password2"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Address', 'rows': 3}),
            'companyname': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'company name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'country'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Phone'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Email Address'}),
            'aadhar_no': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Aadhar no'}),
            'pan_no': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'pan no'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px;', 'placeholder': 'Reenter password'}),

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class WorkForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title','description','skills_required','budget','category','tags','deadline']
        
class WorkForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skills_required', 'budget', 'category', 'tags', 'deadline']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;', 'rows': 3}),
            'skills_required': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;'}),
            # Add border to deadline field
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 5px; border: 1px solid #ccc;'})
        }
    