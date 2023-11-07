from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, "Lin/index.html")
