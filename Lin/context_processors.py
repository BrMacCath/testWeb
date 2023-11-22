from .models import Topic
from django.conf import settings

def Lin_Topics(request):
    return {'Lin_Topics': Topic.objects.all()} 