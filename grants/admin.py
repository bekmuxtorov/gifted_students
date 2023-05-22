from django.contrib import admin
from django.utils.html import format_html

from . import models

# Register your models here.


@admin.register(models.Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date',
                    'download_statute', 'status')
    search_fields = ('name', 'description')
    list_editable = ('status',)
    ordering = ('-create_at',)

    def download_statute(self, obj):
        return format_html(f"<a href='{obj.statute.url}'>Ko'rish</a>")
    download_statute.short_description = 'Nizomni ko\'rish'


@admin.register(models.ScienceDirection)
class GrantStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'grant', 'research_advisor')
    search_fields = ('student', 'research_advisor')
    list_filter = ('student', 'grant')
    ordering = ('-create_at',)
