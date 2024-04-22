from django.urls import path
from buyerapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('signup/',views.RegView.as_view(),name="buyersignup"),
    path('login/',views.SignInView.as_view(),name="buyersignin"),
    path('logout/',views.signoutview,name="buyersignout"),
    path('home/',views.HomeView.as_view(),name="buyerhome"),
    path('addwork/',views.WorkView.as_view(),name="addwork"),
    path('works/',views.WorkListView.as_view(),name="listwork"),
    path('bids/',views.BidsListView.as_view(),name="bids"),
    path('acceptedbids/',views.AcceptedBidsListView.as_view(),name="acceptedbids"),
    path('completedworks/',views.CompWorkListView.as_view(),name="completedworks"),
    path("bids/<int:pk>/approve/",views.approve_bid,name="approve_bid"),
    path('payments/',views.PaymentsListView.as_view(),name="buyerpayments"),
    path('payments/<int:pk>/refundrequest/',views.refund_request,name="refundrequest"),
    path('create_payment/', views.create_payment, name='create_payment'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)