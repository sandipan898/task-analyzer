from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class List(models.Model):
    user = models.ForeignKey(User, related_name="list_user", on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length = 300, blank=True, null=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    time_added = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    time_worked = models.FloatField(blank=True, null=True)
    points = models.IntegerField(default=25, blank=True, null=True)
    weight = models.IntegerField(default=1, blank=True, null=True)
    status = models.CharField(max_length = 300, blank=True, null=True)
    
    @property
    def get_score(self):
        return self.weight*self.score

    def __str__(self):
        return f"{self.item} : {self.is_completed}"


class TimeDivision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 300, blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} : {self.start_time} - {self.end_time}"


def calculate_score(tasks):
    if tasks:
        total_score = 0
        current_score = 0

        for task in tasks:
            total_score += task.get_score
            current_score += task.get_score if task.is_completed else 0
        
        return current_score / total_score * 1000 
    else:
        return None
