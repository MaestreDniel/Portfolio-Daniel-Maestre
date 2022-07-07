from django.urls import path
from portfolio import views


# app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("proyectos/", views.PortfolioListView.as_view()),
    path("proyectos/<project_slug>/", views.ProjectDetailView.as_view()),
]
