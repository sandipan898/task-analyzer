from django.urls import path
from django.views.generic import TemplateView
from .views import (
    delete, DashboardView, 
    done, undone, update, ManageListView,
     HomeView
)
# from .apis import ListUpdateAPI


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('task-manager/', ManageListView.as_view(), name='task-manager'),    

    path('delete/<int:id>', delete, name='delete'),
    path('done/<int:id>', done, name='mark_done'),
    path('undone/<int:id>', undone, name='mark_undone'),
    # path('update/<str:name>', ListUpdateAPI.as_view(), name='update'),
    path('update/<int:id>', update, name='update'),

    path('about/', TemplateView.as_view(template_name='todo/about.html'), name='about'),
    path('help/', TemplateView.as_view(template_name='todo/help.html'), name='help'),
    path('contact/', TemplateView.as_view(template_name='todo/contact.html'), name='contact'),
]