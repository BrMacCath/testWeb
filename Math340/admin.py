from django.contrib import admin

from .models import Choice, Question, Week

class WeekAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Homework", {"fields": ["week_homework","week_homework_description","weight"]}),
        ("Quiz",{"fields":["week_quiz_boolean","week_quiz_location","week_quiz_title"]}),
        ("Website Template",{"fields":["week_web_text","week_worksheet"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["week_homework", "week_quiz_location", "week_web_text"]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Week, WeekAdmin)