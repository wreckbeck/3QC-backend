from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Survey
from .forms import SurveyForm



def index(request):
    return render(request, "survey/index.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)

    form = SurveyForm(survey)
    submitted = False 
    url = reverse("show-survey", args=(id, ))
    if request.method == "POST":
      form = SurveyForm(survey, request.POST)
      if form.is_valid() and form.is_bound:
        form.save()
        return HttpResponseRedirect(url + "?submitted=True")
    else:
      if 'submitted' in request.GET:
        submitted = True
      
    return render(request, 'survey/survey.html', {'survey': survey, 'form': form, 'submitted': submitted})

