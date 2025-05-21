
from django.urls import path,include 
from .views import *
urlpatterns=[
    path("accounts",include("django.contrib.auth.urls")),
    path("registro/singup",SignUpView.as_view(),name="signup"),
    path("",HomeView.as_view(),name="home")
]
