from django.contrib import admin
from .models import Day,Week,Quiz
from django.utils.translation import ngettext
import random
# Register your models here.

weekday_with_class=[("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Friday","Friday")]



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

@admin.action(description="Make quiz week")
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
    
@admin.action(description="Remove quiz week")
def not_quiz_week(self, request, queryset):
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

class QuizInline(admin.TabularInline):
    model = Quiz
    list_display = ["quiz_num"]
    extra = 0


class WeekAdmin(admin.ModelAdmin):
    fieldsets =[ ("Overall Week Details",{"fields": ["week_num","week_title","week_description","pub_date"]}  ),
                 ("Quiz Details",{"fields": ["quiz_Boolean","quiz_description"]}), ]
    list_display = ["week_num","week_title","is_published"]
    actions = [make_published,quiz_week,not_quiz_week]
    inlines =[DayInline,QuizInline]

class QuizAdmin(admin.ModelAdmin):
    fieldsets =[ ("Quiz Identification",{"fields": ["quiz_num"]}  ),
                 ("Quiz Preparation",{"fields": ["description","Rubric_source"]}), 
                 ("Quiz Review",{"fields":["release_answers_date","quiz_here_source","quiz_answer_source"]}) ]
    list_display = ["quiz_num","description","release_answers_date","release_answer_key"]
    list_filter = ["release_answers_date"]




admin.site.register(Week,WeekAdmin)
admin.site.register(Quiz,QuizAdmin)