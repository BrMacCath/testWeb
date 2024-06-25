from django.db import models

# Create your models here.
class Subject(models.Model):
    sub_name = models.CharField(default="None",max_length=40)
    sub_template = models.CharField(default="#",max_length=50)
    description= models.CharField(default="None",max_length=40)
    weight = models.IntegerField(default=0)
    class Meta:
        ordering = ["weight"]
        

class Topic(models.Model):
    sub_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic_name = models.CharField(default="None",max_length=40)
    topic_template  = models.CharField(default="#",max_length=50)
    description= models.CharField(default="None",max_length=40)
    weight = models.IntegerField(default=0)
    class Meta:
        ordering = ["sub_name","weight"]

class Unit(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    unit_name = models.CharField(default="None",max_length=40)
    unit_template = models.CharField(default="#",max_length=50)
    description= models.CharField(default="None",max_length=40)
    weight = models.IntegerField(default=0)
    class Meta:
        ordering = ["topic_name","weight"]