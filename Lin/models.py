from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
import uuid

# Create your models here.
class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic_location = models.CharField(max_length=100,default="test")
    weight = models.PositiveBigIntegerField(default=0)
    topic_webpage = models.CharField(max_length=100,default="Not described")
    topic_description = models.CharField(max_length=100,default="Not described")
    topic_title = models.CharField(max_length=100,default="test")
    class Meta:
        ordering = ["weight"]

    @admin.display(
        boolean=True,
        ordering="weight",
    )
    def __str__(self):
        return self.topic_location