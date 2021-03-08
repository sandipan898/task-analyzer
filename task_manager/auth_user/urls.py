from django.urls import path
from .views import UserSignupView
from .forms import  UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path('home/', user_home_view, name='user_home'),
    path(
        'auth/login/', 
        LoginView.as_view(
            template_name="auth_user/login.html",
            authentication_form=UserLoginForm,
        ), 
        name='user-login'
    ),
    path('auth/logout/', LogoutView.as_view(), name='user-logout'),
    path('auth/signup/', UserSignupView.as_view(), name='user-signup'),
]
