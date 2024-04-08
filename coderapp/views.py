from django.db.models.query import QuerySet
from django.shortcuts import render
from coderapp.forms import *
from adminapp.models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.generic import CreateView,TemplateView,FormView,ListView
from django.views import View




class SignupView(CreateView):
    template_name="coderapp/register.html"  
    model=Coder
    form_class=RegistrationForm
    success_url=reverse_lazy("codersignin")
    
    


class HomeView(TemplateView):
    template_name = "coderapp/home.html"




class SignInView(FormView):
    template_name="coderapp/login.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"failed to login")
                return render(request,self.template_name,{"form":form}) 



class IndexView(TemplateView):
    template_name = "coderapp/index.html"



class CollaboratorView(FormView):
    template_name = "coderapp/collabarator.html"
    form_class = CollaboratorForm
    success_url = reverse_lazy("collaborator")

    def form_valid(self, form):
        id=self.request.user.id
        user_id=Coder.objects.get(id=id)
        form.instance.coder=user_id
        form.save()
        messages.success(self.request, "Code shared successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Code shared failed")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collaborators"] = Collaborate.objects.all()
        context["collaborator"] = Collaborate.objects.exclude(coder=self.request.user.id)

        return context
    
def remove_project(request,*args,**kwargs):
    id=kwargs.get("pk")
    Collaborate.objects.filter(id=id).delete()
    return redirect("collaborator")




class AcceptedBids(ListView):
    template_name="coderapp/bids.html"
    model=Bid
    context_object_name="bids"

    def get_queryset(self):
        current_user=self.request.user.id
        queryset=Bid.objects.filter(coder=current_user,status='True')
        return super().get_queryset()









def SignOutView(request,*args,**kwargs): 
    logout(request)
    return redirect('codersignin')

