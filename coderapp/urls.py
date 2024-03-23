from django.urls import path
from coderapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.SignInView.as_view(),name="signin"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)