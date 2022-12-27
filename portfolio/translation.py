from modeltranslation.translator import translator, TranslationOptions
from portfolio.models import Project

# Project model
class ProjectTranslationOptions(TranslationOptions):
    fields = ('content',)  # Fields that will be translated. Comma is necessary

translator.register(Project, ProjectTranslationOptions)

# It's possible to add any other model