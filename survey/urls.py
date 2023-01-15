from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<int:id>', views.show_survey, name="show_survey"),
    path("survey_csv", views.survey_csv, name="survey_csv"),
]