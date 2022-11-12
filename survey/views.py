from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Survey
from .forms import SurveyForm

def index(request):
    return render(request, "survey/survey.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    form = SurveyForm(survey)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "survey/survey.html", context)