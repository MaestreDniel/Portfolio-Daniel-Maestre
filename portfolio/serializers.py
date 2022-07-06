from rest_framework import serializers
from portfolio.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "thumbnail",
            "content",
            "slug",
            "published",
            "author",
            "status",
        )
