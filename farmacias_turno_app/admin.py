from django.contrib import admin
from .models import *


class ComunaAdmin(admin.ModelAdmin):
    list_display = ['name', 'provincia']
    list_display_links = ['name', 'provincia']
    list_per_page = 20
    search_fields = ['name']


class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'comuna']
    list_display_link = ['nombre', 'comuna']
    list_per_page = 20
    search_fields = ['name']


admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)