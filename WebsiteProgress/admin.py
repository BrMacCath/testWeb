from django.contrib import admin
from .models import Phase
# Register your models here.

class PhaseAdmin(admin.ModelAdmin   ):
    list_display =['title_text','phase_description']

admin.site.register(Phase,PhaseAdmin)