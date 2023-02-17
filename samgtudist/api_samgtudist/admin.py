from django.contrib import admin

from .models import File, Subject, Team, Paragraph


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', "subject_title",)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "file_type")


admin.site.register(Team)
admin.site.register(Paragraph)
