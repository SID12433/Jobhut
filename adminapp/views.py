from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator

from django.db.models import Count
from datetime import date
from django.db.models import Sum





def signin_required(fn):    
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session!..please login")
            return redirect("adminsignin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"Permission denied for current user !")
            return redirect("adminsignin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,is_admin]


class SignInView(View):
    template_name="adminapp/login.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    
    def post(self, request, *args, **kwargs):
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        if uname and pwd:
            usr = authenticate(request, username=uname, password=pwd)
            if usr is not None:
                login(request, usr)
                messages.success(request, "Login success")
                return redirect("adminhome")
        
        messages.error(request, "Failed to login")
        return render(request, self.template_name)
    

@method_decorator(decs,name="dispatch")    
class HomeView(TemplateView):
    template_name = "adminapp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Project.objects.aggregate(count=Count('id'))['count']
        context['sale'] = Payment.objects.aggregate(count=Count('id'))['count']
        context['freelancers'] = Coder.objects.all().count()
        context['buyers'] = Buyer.objects.all().count()
        return context 
    
    
@method_decorator(decs,name="dispatch") 
class CoderView(ListView):
    template_name="adminapp/freelancers.html"
    model=Coder
    context_object_name="freelancers"
    
@method_decorator(decs,name="dispatch") 
class BuyerView(ListView):
    template_name="adminapp/buyers.html"
    model=Buyer
    context_object_name="buyers"
    
    
@method_decorator(decs,name="dispatch") 
class SkillsView(CreateView,ListView):
    template_name="adminapp/skills.html"
    model=Skills
    form_class=SkillForm
    context_object_name="skills"
    success_url=reverse_lazy("skills")

    def form_valid(self, form):
        messages.success(self.request,"skills added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"skills adding failed")
        return super().form_invalid(form)
    

   
def deactivate_skill(request,*args,**kwargs):
    id=kwargs.get("pk")
    Skills.objects.filter(id=id).update(status=False)
    messages.success(request,"skill is now inactive")
    return redirect("skills") 

def activate_skill(request,*args,**kwargs):
    id=kwargs.get("pk")
    Skills.objects.filter(id=id).update(status=True)
    messages.success(request,"skill is now active")
    return redirect("skills")
    

    
@method_decorator(decs,name="dispatch") 
class ProjectsView(ListView):
    template_name="adminapp/projects.html"
    model=Project
    context_object_name="projects" 
    
    
@method_decorator(decs,name="dispatch") 
class PaymentsView(ListView):
    template_name="adminapp/payments.html"
    model=Payment
    context_object_name="payments"
    
    
def signoutview(request,*args,**kwargs):
    logout(request)
    return redirect("adminsignin")