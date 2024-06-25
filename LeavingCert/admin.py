from django.contrib import admin
from .models import Subject,Topic,Unit
# Register your models here.

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 0

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0

class SubjectAdmin(admin.ModelAdmin):
    fieldsets =[ ("Main Subject Details",{"fields": ["sub_name","description","sub_template","weight"]}  ), ]
    inlines = [TopicInline]
    list_display= ["sub_name","weight"]
    extra = 0

class TopicAdmin(admin.ModelAdmin):
    fieldsets =[ ("Main Topic Details",{"fields": ["topic_name","description","topic_template","weight"]}  ), ]
    list_display= ["topic_name","weight"]
    inlines = [UnitInline]

class UnitAdmin(admin.ModelAdmin):
    fieldsets =[ ("Main Uniy Details",{"fields": ["unit_name","description","unit_template","weight"]}  ), ]
    


admin.site.register(Subject,SubjectAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Unit,UnitAdmin)