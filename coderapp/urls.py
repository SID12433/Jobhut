from django.urls import path
from coderapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("",views.HomeView.as_view(),name="coderhome"),
    path("login/",views.SignInView.as_view(),name="codersignin"),
    path("logout/",views.SignOutView,name="codersignout"),
    path("register/",views.SignupView.as_view(),name="codersignup"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("collaborator/",views.CollaboratorView.as_view(),name="collaborator"),
    path("collaborate/<int:pk>/remove/",views.remove_project,name="project-remove"),
    path("bids/",views.AcceptedBids.as_view(),name="bids-list"),
    path("projects/",views.ProjectsListView.as_view(),name="projects-list"),
    path('projects/<int:pk>/make_bid/', views.AddBidFormView.as_view(), name='bid-add'),
    path('bids/<int:pk>/add_work/', views.AddWorkFormView.as_view(), name='biddetail-add'),
    path("profile/",views.ProfileView.as_view(),name="profiles"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)