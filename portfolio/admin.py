from django.contrib import admin
from portfolio.models import Project
from modeltranslation.admin import TranslationAdmin

class ProjectAdmin(TranslationAdmin):
    pass  # No need to code here, just inheritance from TranslationAdmin

# Register your models here.
admin.site.register(Project, ProjectAdmin)
