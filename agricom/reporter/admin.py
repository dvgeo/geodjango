from django.contrib import admin
from .models import Incidence, County

class IncidenceAdmin(admin.ModelAdmin):
    list_display = ('title','date_reported','location')
    search_fields = ('title',)
    filter_fields = ('title','date_reported')

class CountyAdmin(admin.ModelAdmin):
    list_display = ('country', )
    search_fields = ('country',)
    filter_fields = ('country',)

admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(County, CountyAdmin)