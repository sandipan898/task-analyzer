from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class List(models.Model):
    user = models.ForeignKey(User, related_name="list_user", on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length = 300, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    time_added = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    work_time = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.item} {self.completed}"
