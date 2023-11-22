from django.contrib import admin

from .models import Topic

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    fieldsets =[ ("Properties",{"fields": ["weight","topic_location","topic_description","topic_webpage", "topic_title"]}  ), ]
    list_display = ["topic_title","topic_description"]

admin.site.register(Topic,TopicAdmin)