from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from django.shortcuts import get_object_or_404, render
from .models import Choice, Question, Week, WorkShop


class IndexView(generic.ListView):
    template_name = "Math340/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "Math340/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "Math340/results.html"

class HomeworkView(generic.DetailView):
    model = Week
    template_name = "Math340/homework.html"



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    week_list = Week.objects.all
    workshop_list = WorkShop.objects.all
    context = {"latest_question_list": latest_question_list, "week_list": week_list, "workshop_list": workshop_list}
    return render(request, "Math340/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "Math340/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "Math340/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "Math340/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("Math340:results", args=(question.id,)))
    
def homework_page(request,week_weight):
    week_page = get_object_or_404(Week,weight=week_weight)
    return render(request, "Math340/homework.html",{"Week":week_page})

def workShop_page(request,weight):
    workshop_page = get_object_or_404(WorkShop,weight=weight)
    return render(request, "Math340/workshop.html",{"workshop":workshop_page})