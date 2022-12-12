from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Survey, Submission
from .forms import SurveyForm
import csv

def survey_csv(request):
  response = HttpResponse(content_type='type/csv')
  response['Content-Disposition'] = 'attachment; filename=answers.csv'

  # Create csv writer
  writer = csv.writer(response)

  # Designate model
  submissions = Submission.objects.all()
  object = Submission.objects.get(participant_email="d@d.test").answer.all()
  print(object)

  for choice in object:
    print(choice)
    number = int(choice.text)

  # Add Column headings to CSV file
  writer.writerow(['Survey', 'Email', 'Answers', 'Score'])

  # Loop through submissions and append to writer
  for submission in submissions:
    score = 0
    answers = [choice for choice in submission.answer.all()]
    choices = [int(choice.text) for choice in submission.answer.all()]
    for choice in choices:
      score += choice
    writer.writerow([submission.survey, submission.participant_email, answers, score])
  
  return response


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
        print(form.data)
        return HttpResponseRedirect(url + "?submitted=True")
    else:
      if 'submitted' in request.GET:
        submitted = True
      
    return render(request, 'survey/survey.html', {'survey': survey, 'form': form, 'submitted': submitted})

