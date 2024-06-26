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
    path("feedbacks/",views.FeedbacksView.as_view(),name="feedbacks"),
    path("payments/",views.PaymentsView.as_view(),name="payments"),
    path("refunds/",views.RefundView.as_view(),name="refunds"),
    path("payments/<int:pk>/release/",views.release_fund,name="release_fund"),
    path("payments/<int:pk>/releaserefund/",views.release_refund,name="release_refund"),
    path("skills/",views.SkillsView.as_view(),name="skills"),
    path("skills/<int:pk>/deactivate/",views.deactivate_skill,name="remove_skill"),
    path("skills/<int:pk>/activate/",views.activate_skill,name="readd_skill"),
    path("logout/",views.signoutview,name="adminsignout"),


    
]