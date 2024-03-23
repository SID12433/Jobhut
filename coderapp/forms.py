from django import forms
from adminapp.models import Coder
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Coder
        exclude = ('usertype',)   
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({'class': 'form-control'})
 
        
class LoginForm(forms.ModelForm):
    class Meta:
        model=Coder
        fields=['email','password']