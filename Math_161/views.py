from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Week,Day,Quiz
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
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
        if q.week == week:
            Quiz_here = True
            Qui = q
    if week.is_published:
        if week.quiz_Boolean:
            context = {"week": week,"Quiz":week.quiz.get(),"quiz_here":Quiz_here}
        else:
            context ={"week": week }
        return render(request, "Math_161/Week.html",context=context)
    else:
        return render(request, "Math_161/not_published.html")

def day(request,week_num,day):
    week= get_object_or_404(Week, week_num=week_num)
    for days in week.days.all():
        if days.__str__() == day:
            worksheet_source = days.day_worksheet_source
            Day_today = days
    if week.is_published:
        context = {"week": week,"week_num":week_num,"day":day,"worksheet_source":worksheet_source,"Day":Day_today}
        return render(request, "Math_161/Day.html",context=context)
    else:
        return render(request, "Math_161/not_published.html")

# class DayView(generic.DetailView):
#     model=Day
#     context_object_name=

def quiz(request,week_num):
    week= get_object_or_404(Week, week_num=week_num)
    quiz = week.quiz.all()[0]
    if week.is_published:
        context = {"quiz":quiz,"week_num":week_num}
        return render(request,"Math_161/Quiz.html",context=context)
    else:
        return render(request, "Math_161/not_published.html")


class QuizView(generic.DetailView):
    model = Quiz
    slug_field = "emp_no"
    slug_url_kwarg = "week_num"
    context_object_name= "quiz"
    template_name = "Math_161/Quiz.html"
#     def get_context_data(self, **kwargs):
#         context = super(generic.DetailView, self).get_context_data(**kwargs)
#         context["week_num"]=

class IndexView(generic.ListView):
    now = timezone.now()
    queryset= Week.objects.filter(pub_date__lt=now)
    context_object_name = "weeks"
    template_name="Math_161/index.html"