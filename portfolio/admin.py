from django.contrib import admin
from portfolio.models import Project, Work
from modeltranslation.admin import TranslationAdmin


class ProjectAdmin(TranslationAdmin):
    pass  # No need to code here, just inheritance from TranslationAdmin


class WorkAdmin(TranslationAdmin):
    pass


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Work, WorkAdmin)
