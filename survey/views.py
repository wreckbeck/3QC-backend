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

  # Add Column headings to CSV file
  writer.writerow(['Survey', 'Email', 'Answers', 'Score'])

  # Loop through submissions and append to writer
  for submission in submissions:
    score = 0
    answers = submission.answer.all()
    answer_list = []
    choices = []

    for answer in answers:
      answer_list.append(f"{answer.question.text}, {answer.text}")
      choices.append(int(answer.text))

    for choice in choices:
      score += choice
    writer.writerow([submission.survey, submission.participant_email, answer_list, score])
  
  return response


def home(request):
    return render(request, "survey/home.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)

    form = SurveyForm(survey)

    submitted = False 
    url = reverse("show_survey", args=(id, ))
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

