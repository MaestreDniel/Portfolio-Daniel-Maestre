from rest_framework import serializers
from portfolio.models import Project, Work

# Serializers define how the data will be shown in the API
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
        )

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = (
            "id",
            "title",
            "company",
            "content",
            "slug",
            "start_date",
            "finish_date",
            "published",
        )
