from django.contrib import admin
from .models import Content, ExamplePage, File, Material, Quote, Subject, Team


# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'material_title', 'material_type',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', "subject_title",)


class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "file_type")


class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "quote_text", "material")


class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "content_text", "material")


class ExamplePageAdmin(admin.ModelAdmin):
    list_display = ("id", "page", "material")


admin.site.register(Material, MaterialAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ExamplePage, ExamplePageAdmin)
admin.site.register(Team)
