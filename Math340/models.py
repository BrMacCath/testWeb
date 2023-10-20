from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
import uuid

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    

class Week(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    week_quiz_boolean = models.BooleanField(default=False)
    week_quiz_location = models.CharField(max_length=100,default="test")
    week_quiz_title = models.CharField(max_length=100,default="test")
    week_homework_description = models.CharField(max_length=100,default="Not described")
    week_worksheet = models.CharField(max_length=100,default="Not described")
    week_web_text = models.CharField(max_length=100,default="test")
    week_homework = models.CharField(max_length=100,default="homework")
    pub_date = models.DateTimeField("date published")
    weight = models.PositiveBigIntegerField(default=0)
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def __str__(self):
        return self.week_web_text
    