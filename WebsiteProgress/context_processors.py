from .models import Phase
from django.conf import settings

def All_Phases(request):
    return {'All_Phases': Phase.objects.all()} 