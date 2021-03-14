from django.contrib import admin
from .models import List, TimeDivision, ScoreStat

# Register your models here.

admin.site.register(List)
admin.site.register(TimeDivision)
admin.site.register(ScoreStat)