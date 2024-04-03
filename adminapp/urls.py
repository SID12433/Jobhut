from django.urls import path
from adminapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/",views.SignInView.as_view(),name="adminsignin"),
    path("home/",views.HomeView.as_view(),name="home"),

    
]