# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


def user_directory_path(instance, filename):
    return 'portfolio/{0}/{1}'.format(instance.title, filename)


class BasePost(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
    objects = models.Manager()  # default manager

    class Meta:
        abstract = True  # Makes this class abstract, so table in DB is not created


class Project(BasePost):

    class ProjectObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    url = models.CharField(max_length=250, null=True)
    projectobjects = ProjectObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class Work(BasePost):

    class WorkObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    company = models.CharField(max_length=250)
    start_date = models.DateField(default=date.today)
    finish_date = models.DateField(blank=True, null=True)
    # stack = models.JSONField()
    author = None  # Remove inherited field
    workobjects = WorkObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


"""class Stack(BasePost):

    class WorkObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    company = models.CharField()
    initial_date = models.DateTimeField()
    finish_date = models.DateTimeField(blank=True, null=True)
    # stack = models.JSONField()
    workobjects = WorkObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title"""
