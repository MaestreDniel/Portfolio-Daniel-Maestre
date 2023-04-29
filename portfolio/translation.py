from modeltranslation.translator import translator, TranslationOptions
from portfolio.models import Project, Work

# Models to be translated
class ProjectTranslationOptions(TranslationOptions):
    fields = ('content',)  # Fields that will be translated. Comma is necessary


class WorkTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Project, ProjectTranslationOptions)
translator.register(Work, WorkTranslationOptions)

# It's possible to add any other model