from django.shortcuts import render
from django.views.generic import *
from buyerapp.forms import *
from adminapp.models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.


def signin_required(fn):    
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session!..please login")
            return redirect("buyersignin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



class RegView(CreateView):
    template_name = "buyerapp/register.html"
    model= Buyer
    form_class = RegForm
    success_url=reverse_lazy("buyersignin")


    def form_valid(self, form):
        form.instance.role = 'coder'
        return super().form_valid(form)   
 
    

class SignInView(FormView):
    template_name="buyerapp/login.html"
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
                return redirect("buyerhome")
            else:
                messages.error(request,"failed to login")
                return render(request,self.template_name,{"form":form})


class HomeView(TemplateView):

    template_name = "buyerapp/home.html"
    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        buyer_id = self.request.user.id
        context["works"] = Project.objects.filter(buyer=buyer_id).count()
        context["completed_works"] = Payment.objects.filter(buyer=self.request.user).count()
        context["payment"] = Payment.objects.filter(buyer=self.request.user).count()
        total_amount = Payment.objects.filter(buyer=self.request.user).aggregate(Sum('amount'))['amount__sum']
        context["Total_Amount"] = total_amount if total_amount else 0
    
        return context
    

class WorkView(CreateView):
    template_name="buyerapp/addpost.html"
    model=Project
    form_class=WorkForm
    success_url=reverse_lazy("addwork")

    def form_valid(self, form):
        id=self.request.user.id
        buyer=Buyer.objects.get(id=id)
        form.instance.buyer = buyer
        messages.success(self.request,"work added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"work adding failed")
        return super().form_invalid(form)


class WorkListView(ListView):
    template_name="buyerapp/works.html"
    model=Project
    context_object_name="projects"
    
    def get_queryset(self):
        current_user = self.request.user
        queryset = Project.objects.filter(buyer=current_user)
        return queryset
    
    
class BidsListView(ListView):
    template_name="buyerapp/bids.html"
    model=Bid
    context_object_name="bids"
    
    def get_queryset(self):  
        current_user = self.request.user
        queryset = Bid.objects.filter(project__buyer=current_user).order_by('-bid_amount')
        return queryset
    

class AcceptedBidsListView(ListView):
    template_name="buyerapp/acceptedbids.html"
    model=Bid
    context_object_name="bids" 
    
    def get_queryset(self):  
        current_user = self.request.user
        queryset = Bid.objects.filter(project__buyer=current_user,status=True)
        return queryset
    

def approve_bid(request,*args,**kwargs):
    id=kwargs.get("pk")
    Bid.objects.filter(id=id).update(status=True)
    messages.success(request,"Bid is approved")
    return redirect("bids") 



    
    
class PaymentsListView(ListView):
    template_name="buyerapp/payments.html"
    model=Payment
    context_object_name="payments"
    
    def get_queryset(self):
        current_user = self.request.user
        queryset = Payment.objects.filter(buyer=current_user)
        return queryset
    
    
def refund_request(request,*args,**kwargs):
    id=kwargs.get("pk")
    Payment.objects.filter(id=id).update(refund=True)
    messages.success(request,"refund requested")
    return redirect("buyerpayments")
    
    
class CompWorkListView(ListView):
    template_name="buyerapp/completedwork.html"
    model=BidDetails
    context_object_name="projects"
    
    def get_queryset(self):
        current_user = self.request.user
        queryset = BidDetails.objects.filter(bid__project__buyer=current_user,bid__payment__isnull=False)
        return queryset



import json
def create_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        buyer_id = data.get('buyer_id')
        coder_id = data.get('coder_id')
        bid_id = data.get('bid_id')
        amount = data.get('amount')

        print("Data received from front end:", data)

        try:
            payment = Payment.objects.create(
                buyer_id=buyer_id,
                coder_id=coder_id,
                bid_id=bid_id,
                amount=amount
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)



def signoutview(request,*args,**kwargs):
    logout(request)
    return redirect("buyersignin")