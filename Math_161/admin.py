from django.contrib import admin
from .models import Day,Week
from django.utils.translation import ngettext
import random
# Register your models here.

weekday_with_class=[(1,"Monday"),(2,"Tuesday"),(3,"Wednesday"),(4,"Friday")]





@admin.action(description="Filled in days")
def make_days(self,request,queryset):
    for day in weekday_with_class:
        pass
    pass

@admin.action(description="Change publish date to today")
def make_published(self, request, queryset):
    quiz_weeks = queryset.update(quiz_Boolean=True)
    self.message_user(
            request,
            ngettext(
                "%d week has a quiz.",
                "%d weeks have quizzes.",
                quiz_weeks,
            )
            % quiz_weeks,
        )

@admin.action(description="Quiz this week")
def quiz_week(self, request, queryset):
    quiz_weeks = queryset.update(quiz_Boolean=True)
    self.message_user(
            request,
            ngettext(
                "%d week has a quiz.",
                "%d weeks have quizzes.",
                quiz_weeks,
            )
            % quiz_weeks,
        )
    
@admin.action(description="Not quiz week")
def quiz_week(self, request, queryset):
    quiz_weeks = queryset.update(quiz_Boolean=False)
    self.message_user(
            request,
            ngettext(
                "%d week does not have a quiz.",
                "%d weeks do not have quizzes.",
                quiz_weeks,
            )
            % quiz_weeks,
        )



class DayInline(admin.TabularInline):
    model = Day
    extra = 0

class WeekAdmin(admin.ModelAdmin):
    fieldsets =[ ("Overall Week Details",{"fields": ["week_num","week_title","week_description"]}  ),
                 ("Quiz Details",{"fields": ["quiz_Boolean","quiz_description"]}), ]
    list_display = ["week_num","week_title"]
    actions = [make_days,make_published,quiz_week]
    inlines =[DayInline]


admin.site.register(Week,WeekAdmin)
