from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import Survey
from .forms import SurveyForm

def index(request):
    return render(request, "survey/index.html")

def show_survey(request, id=None): # form data is sent back to view and processed here as well
    survey = get_object_or_404(Survey, pk=id)
    # if this is a POST request, we need to process the form data and create a form instance that is
    # populated with the data from the request
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)
    
    url = reverse("show-survey", args=(id, ))
    # We need to check if the data is valid
    if form.is_bound and form.is_valid():
      form.save()
      messages.add_message(request, messages.INFO, 'Submission saved.')
      return redirect(url)
    else:
      form 

    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "survey/survey.html", context)