from django.urls import path
from .views import (
    dashboard_view, delete, DashboardView, 
    done, undone, update, 
    help_view, about_view, contact_view, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('about/', about_view, name='about'),
    path('help/', help_view, name='help'),
    path('contact/', contact_view, name='contact'),
    path('delete/<int:id>', delete, name='delete'),
    path('done/<int:id>', done, name='mark_done'),
    path('undone/<int:id>', undone, name='mark_undone'),
    path('update/<int:id>', update, name='update'),
]