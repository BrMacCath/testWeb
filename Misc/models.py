from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
import uuid
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=30)
    topic_weight= models.IntegerField()


class Section(models.Model):
    section_name = models.CharField(max_length=30) 
    section_weight= models.IntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class Notes(models.Model):
    note_name = models.CharField(max_length=30) 
    note_weight= models.IntegerField()
    section= models.ForeignKey(Section,on_delete=models.CASCADE)

