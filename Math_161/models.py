from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
import uuid

from django.utils.timezone import make_aware
# Create your models here.

weekday_with_class=[(1,"Monday"),(2,"Tuesday"),(3,"Wednesday"),(4,"Friday")]

## Week Model
# This should have several characteristics.
# 1. The week number
# 2. The location of each of the index webpage.
# 3. A general description of what is going on in that week.
# 4. Create four instances of day with each instance of 
# weekday_with_class used.
# 5. Week title will be a short description for the sidebar navigation.
# 6. Create a way to check when you should publish the notes.

class Week(models.Model):

    def get_mytimezone_date(original_datetime):
        new_datetime = datetime.strptime(original_datetime, '%Y-%m-%d')
        tz = timezone.get_current_timezone()
        timzone_datetime = timezone.make_aware(new_datetime, tz, True)
        return timzone_datetime.date()
    # Overall week details. Pub date is when the week is published
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    week_num = models.IntegerField(default=0)
    week_webpage_source= models.CharField(default="test",max_length=50)
    week_title = models.CharField(default="test",max_length=300)
    week_description = models.CharField(default="test",max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    # This is for the weeks where there are quizzes
    quiz_Boolean = models.BooleanField(default=False)
    quiz_description= models.CharField(default="None",max_length=20)
    
    class Meta:
        ordering =["week_num"]

    def create_week(self):
        #This will create the day and the html source
        for day in weekday_with_class:
            class_day = Day(week=self,day=day[0])
            class_day.save()



## The day model
# The day model should only connect with one week model.
# The day should only be able to choose between Monday, Tuesday
# Wednesday and Friday as those are the only days we have class.
# 

class Day(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(default=(1,"Monday"),choices=weekday_with_class)
    day_webpage_source= models.CharField(default="test",max_length=50)
    day_description = models.CharField(default="test",max_length=300)
