from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("survey/1", views.show_survey, name="show_survey"),
    path("survey/survey_csv", views.survey_csv, name="survey_csv"),
]