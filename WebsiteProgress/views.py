from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from django.shortcuts import get_object_or_404, render
from .models import Phase

class IndexView(generic.ListView):
    template_name = "WebsiteProgress/index.html"
    context_object_name = "phase_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Phase.objects.order_by("id")

class phaseView(generic.DetailView):
    model = Phase
    template_name = "WebsiteProgress/phase.html"


def index(request):
    phase_list = Phase.objects.order_by("id")
    context = {"phase_list": phase_list}
    return render(request, "WebsiteProgress/index.html", context)

def phase(request,phase_id):
    phase = get_object_or_404(Phase,pk=phase_id)
    return render(request, "WebsiteProgress/phase.html", {"phase": phase})
