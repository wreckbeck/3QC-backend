from django.contrib import admin

from .models import Submission, Survey, Choice, Question

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True

# TabularInLine exposes the model to the Parent / Foreign Key relation model, making it possible to 
# add, remove, or edit model directly from Parent / Foreign Key
class ChoiceInline(admin.TabularInline):
  model = Choice


class SurveyAdmin(admin.ModelAdmin):
  inlines = [
    QuestionInline
  ]

class QuestionAdmin(admin.ModelAdmin):
  inlines = [
    ChoiceInline
  ]
  
class SubmissionAdmin(admin.ModelAdmin):
  list_display = ('participant_email', 'status')

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
