from django.contrib import admin
from .models import Material, Subject, File, Quote, Content, ExamplePage


# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_title', 'material_type',)


admin.site.register(Material, MaterialAdmin)
admin.site.register(Subject)
admin.site.register(File)
admin.site.register(Quote)
admin.site.register(Content)
admin.site.register(ExamplePage)
