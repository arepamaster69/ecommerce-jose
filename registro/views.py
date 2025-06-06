from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

# Create your views here.


class SignUpView(CreateView):

    template_name="registration/signup.html"
    form_class=UserCreationForm
    success_url= reverse_lazy("login")

class HomeView(TemplateView):
    template_name='registration/home.html'

    