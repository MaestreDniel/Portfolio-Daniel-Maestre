from django.urls import path
from portfolio import views

""" urlpatterns = [
    path('', views.index, name='index'),
] """


from portfolio.views import PortfolioListView, ProjectDetailView

app_name = "portfolio"

urlpatterns = [
    path("proyectos/", PortfolioListView.as_view()),
    path("proyectos/<project_slug>/", ProjectDetailView.as_view()),
]
