from django.contrib import admin

from .models import Content, ExamplePage, File, Subject, Team


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', "subject_title",)


class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "file_type")


class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "content_text", "material")


class ExamplePageAdmin(admin.ModelAdmin):
    list_display = ("id", "page", "material")


admin.site.register(Subject, SubjectAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ExamplePage, ExamplePageAdmin)
admin.site.register(Team)
