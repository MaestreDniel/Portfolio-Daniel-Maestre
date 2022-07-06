# Create your views here.

""" def index(request):
    context = {}

    return render(request, 'portfolio/index.html', context) """

from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response

from portfolio.models import Project
from portfolio.serializers import ProjectSerializer


class PortfolioListView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.projectobjects.all()[0:4] # Paginación con 0:4
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    def get(self, request, project_slug, *args, **kwargs):
        project = get_object_or_404(Project, slug=project_slug)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
