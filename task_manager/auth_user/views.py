from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from django.urls import reverse, reverse_lazy
from .forms import SignupUserForm
from django.views import generic


# def user_home_view(request):
#     template_name = "app_user/user_home.html"
#     context = {}
#     return render(request, template_name, context)

class UserSignupView(generic.CreateView):
    form_class = SignupUserForm
    template_name = "authuser/signup.html"
    success_url = reverse_lazy('user-login')

