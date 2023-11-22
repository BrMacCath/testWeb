from .models import Topic
from django.conf import settings

def All_Topics(request):
    return {'All_Topics': Topic.objects.all()} 