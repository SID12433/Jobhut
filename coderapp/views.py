from django.db.models.query import QuerySet
from django.shortcuts import render
from coderapp.forms import *
from adminapp.models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.generic import CreateView,TemplateView,FormView,ListView,DetailView,UpdateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView




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


from django.db.models import Sum
class IndexView(TemplateView):
    template_name = "coderapp/index.html"
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        coder_id = self.request.user.id
        context["works"] = Bid.objects.filter(coder=coder_id, status=True).count()
        context["collaborator"] = Collaborate.objects.exclude(coder=coder_id)
        context["completed_works"] = Coder.objects.filter(id=coder_id, status=True).count()
        context["payment"] = Payment.objects.filter(coder=self.request.user).count()
        total_amount = Payment.objects.filter(coder=self.request.user).aggregate(Sum('amount'))['amount__sum']
        context["Total_Amount"] = total_amount if total_amount else 0
    
        return context        
    

        



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
        context["collaborators"] = Collaborate.objects.filter(coder=self.request.user.id)
        context["collaborator"] = Collaborate.objects.exclude(coder=self.request.user.id)

        return context
    
def remove_project(request,*args,**kwargs):
    id=kwargs.get("pk")
    Collaborate.objects.filter(id=id).delete()
    return redirect("collaborator")



class ProjectsListView(ListView):
    template_name="coderapp/recentworks.html"
    model=Project
    context_object_name="projects"
    
    
from django.shortcuts import get_object_or_404

class AddBidFormView(FormView):
    form_class = AddBidForm
    template_name = 'your_template.html' 

    def form_valid(self, form):
        bid_amount = form.cleaned_data['bid_amount']
        note = form.cleaned_data['note']
        coder = get_object_or_404(Coder, pk=self.request.user.id)
        
        bid = Bid.objects.create(
            
            coder=coder, 
            project_id=self.kwargs['pk'],  
            bid_amount=bid_amount,
            note=note
        )
        
        
        return HttpResponseRedirect(reverse('projects-list')) 

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class AcceptedBids(ListView):
    template_name="coderapp/bids.html"
    model=Bid
    context_object_name="bids"

    def get_queryset(self):
        current_user=self.request.user.id
        queryset=Bid.objects.filter(coder=current_user,status=True)
        return queryset



class AddWorkFormView(FormView):
    form_class = AddWorkForm
 
    def form_valid(self, form):
        coder = get_object_or_404(Coder, pk=self.request.user.id)
        bid_id = self.kwargs['pk']
        bid_detail = Bid.objects.get(id=bid_id)
        
        work = BidDetails.objects.create(
            coder=coder,
            bid=bid_detail,
            doc=form.cleaned_data['doc']
        )

        bid_detail.progress = "Completed"
        bid_detail.save()

        return HttpResponseRedirect(reverse('bids-list'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



from django.shortcuts import get_object_or_404

class ProfileView(DetailView,UpdateView):
    template_name="coderapp/profile.html"
    model=Coder
    form_class=ProfileUpdateForm
    context_object_name="p"
    success_url=reverse_lazy("profiles")

    def get_object(self, queryset=None):
        current_user_id = self.request.user.id
        coder_instance = get_object_or_404(Coder, id=current_user_id)
        return coder_instance



def SignOutView(request,*args,**kwargs): 
    logout(request)
    return redirect('codersignin')

