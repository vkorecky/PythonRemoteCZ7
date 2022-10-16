from django.contrib import admin
from django.contrib.admin import ModelAdmin

from base.models import Room, Message


class RoomAdmin(ModelAdmin):
    # FormView
    fieldsets = [
        (None, {'fields': ['id', 'name', 'created', 'updated']}),
        (
            'Detail',
            {
                'fields': ['description'],
                'description': (
                    'Detailed information about room'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['participants'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created', 'id', 'updated']

    # ListView
    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['name']
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name']
    list_per_page = 20
    list_filter = ['name']
    search_fields = ['name', 'description']
    actions = ['cleanup_description']


# Register your models here.
admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
