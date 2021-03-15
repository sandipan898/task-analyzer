from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class List(models.Model):
    user = models.ForeignKey(User, related_name="list_user", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 300, blank=True, null=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    time_added = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    time_worked = models.FloatField(blank=True, null=True)
    points = models.IntegerField(default=25, blank=True, null=True)
    weight = models.IntegerField(default=1, blank=True, null=True)
    status = models.CharField(default="Work not Completed", max_length = 300, blank=True, null=True)
    
    @property
    def get_score(self):
        return self.weight*self.points

    def __str__(self):
        return f"{self.name} : {self.is_completed}"


class TimeDivision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 300, blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} : {self.start_time} - {self.end_time}"

class ScoreStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    current_score = models.IntegerField(default=0, blank=True, null=True)
    seven_days_score = models.CharField(max_length=300, blank=True, null=True)
    score_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    @property
    def refresh_score(self): 
        if self.current_score:
            time_difference = self.score_date.timestamp() - datetime.datetime.now().timestamp()
            print(time_difference)
            if abs(time_difference) > 24:
                self.seven_days_score + str(self.current_score) + ' '
                print(self.seven_days_score)

                self.current_score = 0

    @property
    def calculate_score(self):
        total_tasks = List.objects.filter(user=self.user).all()
        print(total_tasks)
        if total_tasks:
            total_score = 0
            current_score = 0

            for task in total_tasks:
                total_score += task.get_score
                current_score += task.get_score if task.is_completed else 0
            self.current_score = current_score / total_score * 1000 
        else:
            self.current_score = 0
    
    @property
    def calculate_seven_days_score(self):
        if self.seven_days_score:
            seven_days_scores = self.seven_days_score.split(' ')
            print(seven_days_scores)
            return seven_days_scores
        
    def __str__(self):
        return f"{self.user} : {self.current_score}"
