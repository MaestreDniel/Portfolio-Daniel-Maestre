# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.utils import translation
from rest_framework.views import APIView
from rest_framework.response import Response

from portfolio.models import Project, Work
from portfolio.serializers import ProjectSerializer, WorkSerializer

def index(request):
    context = {}

    return render(request, 'portfolio/index.html', context)


def handle_http_accept_lang(self):
    """
    Handle header for user locale, get substring for tne first two chars
    """
    if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
        lang = self.request.META['HTTP_ACCEPT_LANGUAGE'][:2]
        translation.activate(lang)


class ProjectListView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.projectobjects.all()[0:4] # Pagination with 0:4

        handle_http_accept_lang(self)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    def get(self, request, project_slug, *args, **kwargs):
        project = get_object_or_404(Project, slug=project_slug)

        handle_http_accept_lang(self)
        
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class WorkListView(APIView):
    def get(self, request):
        works = Work.workobjects.all()[0:4] 

        handle_http_accept_lang(self)

        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)