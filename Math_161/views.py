from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Week,Day,Quiz
from django.shortcuts import get_object_or_404, render

def index(request):
    Weeks = Week.objects.all()
    context = {"weeks":Weeks}
    return render(request, "Math_161/index.html",context=context)

def week(request,week_num):
    week= get_object_or_404(Week, week_num=week_num)
    # Check if there is a quiz linked into this week
    quiz = Quiz.objects.all().prefetch_related("week")
    Quiz_here = False
    Qui = None
    for q in quiz:
        if q.week.week_num == week.week_num:
            Quiz_here = True
            Qui = q
    if week.quiz_Boolean:
        return render(request, "Math_161/Week.html",{"week": week,"Quiz":Qui,"quiz_here":Quiz_here})
    else:
        return render(request, "Math_161/not_published.html")

def day(request,week_num,day):
    week= get_object_or_404(Week, week_num=week_num)
    if week.quiz_Boolean:
        tempDay= Day.objects.filter(day=day).prefetch_related("week")
        # tempDay = tempDay.objects.get(week_num=week_num)
        context = {"week": week,"week_num":week_num,"day":day,"worksheet_source":tempDay}
        return render(request, "Math_161/Day.html",context=context)
    else:
        return render(request, "Math_161/not_published.html")

def quiz(request,quiz_num):
    quiz= get_object_or_404(Quiz, quiz_num=quiz_num)
    return render(request,"Math_161/quiz.html",{"quiz":quiz})

