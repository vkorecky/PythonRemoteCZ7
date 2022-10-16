from django.contrib import admin
from django.contrib.admin import ModelAdmin

from base.models import Room, Message


class MessageAdmin(ModelAdmin):
    # FormView
    fieldsets = [
        (None, {'fields': ['id', 'body']}),
        (
            'Detail',
            {
                'fields': ['room', 'created', 'updated'],
                'description': (
                    'Detailed information about room'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['user'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created', 'id', 'updated']

    # ListView
    @staticmethod
    def cleanup_body(modeladmin, request, queryset):
        queryset.update(body="-- Deleted --")

    ordering = ['id']
    list_display = ['id', 'body', 'room']
    list_display_links = ['id']
    list_per_page = 20
    list_filter = ['room']
    search_fields = ['body', 'room']
    actions = ['cleanup_body']


# Register your models here.
admin.site.register(Room)
admin.site.register(Message, MessageAdmin)
