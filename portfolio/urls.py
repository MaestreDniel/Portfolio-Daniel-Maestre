from django.urls import path
from portfolio import views


# app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.ProjectListView.as_view()),
    path("projects/<project_slug>/", views.ProjectDetailView.as_view()),
    path("works/", views.WorkListView.as_view())
]
