from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

from django.conf import settings
import uuid

from django.utils.timezone import make_aware
# Create your models here.

weekday_with_class=[("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Friday","Friday")]


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
    pub_date = models.DateTimeField("date published")

    # This is for the weeks where there are quizzes
    quiz_Boolean = models.BooleanField(default=False)
    quiz_description= models.CharField(default="None",max_length=20)
    
    class Meta:
        ordering =["week_num"]

    @property
    def is_published(self):
        now = timezone.now()
        return self.pub_date <= now



## The day model
# The day model should only connect with one week model.
# The day should only be able to choose between Monday, Tuesday
# Wednesday and Friday as those are the only days we have class.
# 

class Day(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE,related_name="days")
    day = models.CharField(default=("Monday","Monday"),choices=weekday_with_class,max_length=10)
    day_worksheet_source= models.CharField(default="#",max_length=100)
    day_description = models.CharField(default="test",max_length=300)
    day_Slides_Boolean = models.BooleanField(default=False)
    day_Slides_Source = models.CharField(default="test",max_length=30)
    def __str__(self) -> str:
        return self.day
    
## The quiz model

# This is going to be the quiz model. 
#
# It will contain the week and quiz num.
# The goal is to have it contain all the info about quizzes 
# such as quiz files, 

class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    week = models.ForeignKey(Week, on_delete=models.CASCADE,related_name="quiz")
    quiz_num = models.IntegerField(default=0)
    quiz_prepsheet_source =  models.CharField(default="#",max_length=100)
    quiz_here = models.BooleanField(default=False)
    quiz_here_source =  models.CharField(default="#",max_length=100)
    description= models.CharField(default="None",max_length=20)



