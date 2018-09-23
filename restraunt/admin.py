from django.contrib import admin
from .models import RestrauntLocation
# Register your models here.


class RestrauntAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "category", "timestamp", "updated"]
    search_fields = ['name', 'location', 'category']
    list_filter = ['name', 'location', 'category']
admin.site.register(RestrauntLocation, RestrauntAdmin)    