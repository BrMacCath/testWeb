from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Topic
from django.shortcuts import get_object_or_404, render

def index(request):
    Lin_Topics = Topic.objects.all
    context ={"Lin_Topics": Lin_Topics}
    return render(request, "Lin/index.html",context=context)

def topic_page(request,weight):
    topic_page = get_object_or_404(Topic,weight=weight)
    return render(request, "Lin/topic.html",{"topic":topic_page})
