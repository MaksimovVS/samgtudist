from django.db import models
from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import Content, ExamplePage, File, Quote, Subject, Team


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', "subject_title",)


class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "file_type")


class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "quote_text", "material")
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }


class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "content_text", "material")


class ExamplePageAdmin(admin.ModelAdmin):
    list_display = ("id", "page", "material")


admin.site.register(Subject, SubjectAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ExamplePage, ExamplePageAdmin)
admin.site.register(Team)
