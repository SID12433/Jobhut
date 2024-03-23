from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView,ListView,UpdateView,DetailView
from coderapp.forms import RegistrationForm,LoginForm
from adminapp.models import Coder
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator



class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    model=Coder
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    
    
class SignInView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        pwd = form.cleaned_data.get("password")
        user = authenticate(self.request, email=email, password=pwd)
        if user:
            login(self.request, user)
            messages.success(self.request, "Login success")
            return redirect("signup")
        else:
            messages.error(self.request, "Failed to login")
            return render(self.request, self.template_name, {"form": form})
      
        
class HomeView(TemplateView):
    template_name="home.html"