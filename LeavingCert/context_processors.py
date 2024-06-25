from .models import Subject
from django.conf import settings

def All_Subs(request):
    return {'All_Subs': Subject.objects.all()} 