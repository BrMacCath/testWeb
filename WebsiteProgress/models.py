from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
import uuid
# Create your models here.
class Phase(models.Model):
    weight = models.PositiveBigIntegerField(default=0) 
    web_text = models.CharField(max_length=20000,default="None")
    title_text =models.CharField(max_length=200,default="Phase")
    phase_description = models.CharField(max_length=100,default="Not yet.") 
    def __str__(self):
        return self.title_text
    
    