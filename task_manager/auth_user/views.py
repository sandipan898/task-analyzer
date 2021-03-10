from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from .forms import SignupUserForm, UserLoginForm
from django.views import generic


class UserSignupView(generic.CreateView):
    form_class = SignupUserForm
    template_name = "auth_user/signup.html"
    success_url = reverse_lazy('/dashboard')


"""
class AuthView(generic.View):
    template_name = "auth_user/index.html"
    form_class = (SignupUserForm, UserLoginForm)
    success_url = reverse_lazy('home')
    
    def get(self, request, *args, **kwargs):
        form1 = SignupUserForm()
        form2 = UserLoginForm()
        context = {} 
        context['signup_form'] = form1
        context['login_form'] = form2
        return render(self.request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print("Login")
        if request.POST.get('submit') == 'Login':
            # your sign in logic goes here
            username = request.POST['username']
            password = request.POST['password']
            form = UserLoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('home') 
                else:
                    return redirect('user-auth')
            else:
                return redirect('user-auth') 

        elif request.POST.get('submit') == 'Sign up':
            # your sign up logic goes here
            print(request.POST)
            print("SignUp")
            form = SignupUserForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                user = form.save(False)
                print(user)
                user.set_password(user.password)
                user.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/') 
        return render(self.request, self.template_name) 
"""