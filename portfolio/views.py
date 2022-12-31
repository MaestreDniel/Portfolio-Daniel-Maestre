# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.utils import translation
from rest_framework.views import APIView
from rest_framework.response import Response

from portfolio.models import Project
from portfolio.serializers import ProjectSerializer

def index(request):
    context = {}

    return render(request, 'portfolio/index.html', context)

class ProjectListView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.projectobjects.all()[0:4] # Pagination with 0:4

        # Header for user locale, get substring for two first chars
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE'][:2]
            translation.activate(lang)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    def get(self, request, project_slug, *args, **kwargs):
        project = get_object_or_404(Project, slug=project_slug)

        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
