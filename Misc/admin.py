from .models import Topic, Section, Notes

from django.contrib import admin

# Register your models here.


class NotesAdmin(admin.TabularInline):
    model = Notes
    fieldsets =[
        ("Note Properties", {"fields":["note_name","note_weight"]})
    ]
    extra=1

class SectionInline(admin.TabularInline):
    model = Section
    fieldsets =[
        ("Section Properties", {"fields":["section_name","section_weight"]})
    ]
    extra=1


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Topic Properties", {"fields": ["topic_name","topic_weight"]}),
    ]
    list_display = ["topic_name"]
    inlines= [SectionInline]

admin.site.register(Topic,TopicAdmin)

class SectionAdmin(admin.ModelAdmin):
    fieldsets =[
        ("Section Properties", {"fields":["section_name","section_weight"]})
    ]
    list_display =["section_name"]
    inlines =[NotesAdmin]

admin.site.register(Section,SectionAdmin)

