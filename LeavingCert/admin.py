from django.contrib import admin
from .models import Subject,Topic,Unit
# Register your models here.

class TopicInline(admin.TabularInline):
    model = Topic


class SubjectAdmin(admin.ModelAdmin):
    fieldsets =[ ("Overall Week Details",{"fields": ["sub_name","weight"]}  ), ]
    inlines = [TopicInline]
    list_display= ["sub_name","weight"]
    extra = 0




admin.site.register(Subject,SubjectAdmin)