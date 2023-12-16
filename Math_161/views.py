from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Week,Day
from django.shortcuts import get_object_or_404, render

def index(request):
    Weeks = Week.objects.all()
    context = {"weeks":Weeks}
    return render(request, "Math_161/index.html",context=context)

def week(request,week_num):
    week= get_object_or_404(Week, week_num=week_num)
    return render(request, "Math_161/Week.html",{"week": week})

def day(request,week_num,day_name,day):
    week= get_object_or_404(Week, week_num=week_num)
    context = {"week": week,"week_num":week_num,"day":day,"day_name":day_name}
    return render(request, "Math_161/Day.html",context=context)

def detail(request, week_id):
    week = get_object_or_404(Week, pk=week_id)
    return render(request, "Math_161/week.html")

