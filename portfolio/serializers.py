from rest_framework import serializers
from portfolio.models import Project

# Aquí se define cómo se representan los datos en la API
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "thumbnail",
            "content",
            "url",
            "slug",
            "published",
            "author",
            "status",
        )
