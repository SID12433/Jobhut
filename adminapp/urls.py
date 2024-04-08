from django.urls import path
from adminapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/",views.SignInView.as_view(),name="adminsignin"),
    path("home/",views.HomeView.as_view(),name="adminhome"),
    path("projects/",views.ProjectsView.as_view(),name="projects"),
    path("coders/",views.CoderView.as_view(),name="coders"),
    path("buyers/",views.BuyerView.as_view(),name="buyers"),
    path("payments/",views.PaymentsView.as_view(),name="payments"),
    path("skills/",views.SkillsView.as_view(),name="skills"),
    path("skills/<int:pk>/deactivate/",views.deactivate_skill,name="remove_skill"),
    path("skills/<int:pk>/activate/",views.activate_skill,name="readd_skill"),
    path("logout/",views.signoutview,name="adminsignout"),


    
]