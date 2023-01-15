from django.contrib import admin

from .models import File, Subject, Team


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', "subject_title",)


class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "file_type")


admin.site.register(Subject, SubjectAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Team)
