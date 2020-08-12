from django.contrib import admin
from .models import *
# Register your models here.


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']
    list_insances = True
    search_fields = ['name']


admin.site.register(Skills, SkillsAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug',]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImages)
