from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
import uuid

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=30)
    topic_weight= models.IntegerField()
    topic_location = models.CharField(max_length=30,default="Default") 
    class Meta:
        ordering = ["topic_weight"]


class Section(models.Model):
    section_name = models.CharField(max_length=30) 
    section_weight= models.IntegerField()
    section_location = models.CharField(max_length=30,default="Default") 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    class Meta:
        ordering = ["section_weight"]

class Notes(models.Model):
    note_name = models.CharField(max_length=30) 
    note_weight= models.IntegerField()
    note_location = models.CharField(max_length=30,default="Default") 
    section= models.ForeignKey(Section,on_delete=models.CASCADE)
    class Meta:
        ordering = ["note_weight"]

