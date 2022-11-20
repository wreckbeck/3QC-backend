from django import forms
from django.forms import ModelForm
from .models import Question

from .models import Choice, Submission, Survey

# form widgets - define html input items. RadioSelect takes an optional 'choices' argument

class SurveyForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class:': 'form-control'})) # define an email field at top of survey

    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey
        for question in survey.questions.all():
            choices = [(choice.id, choice.text) for choice in question.choices.all()]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-control'}), choices=choices)
            self.fields[f"question_{question.id}"].label = question.text

    def save(self):
        data = self.cleaned_data # dictionary, contains form data
        submission = Submission(survey=self.survey, participant_email=data["email"])
        submission.save()
        for question in self.survey.question_set.all():
            choice = Choice.objects.get(pk=data[f"question_{question.id}"])
            submission.answer.add(choice)
      
        submission.save()
        return submission
