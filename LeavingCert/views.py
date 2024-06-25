from django.shortcuts import get_object_or_404, render,redirect
from .models import Subject,Topic,Unit
# Create your views here.
def index(request):
    return render(request, "LeavingCert/index.html")

def subPage(request,sub_name):
    subject= get_object_or_404(Subject, sub_name=sub_name)
    topics = subject.topic_set.all()
    context = {"sub":subject,"topics":topics}
    return render(request,"LeavingCert/subject.html",context=context)

def topicPage(request,sub_name,topic_name):
    topic= get_object_or_404(Topic, topic_name=topic_name)
    context = {"topic":topic}
    return render(request,"LeavingCert/topic.html",context=context)

def unitPage(request,sub_name,topic_name,unit_name):
    unit= get_object_or_404(Topic, unit_name=unit_name)
    context = {"unit":unit}
    return render(request,"LeavingCert/unit.html",context=context)