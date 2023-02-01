from django.contrib import admin
from django.urls import path
from django.utils.safestring import mark_safe

from .forms import MediaForm
from .models import (Announcement, Configuration, Media, Planning, Room,
                     Teacher, Time)


# Admin interface for the media
class MediaAdmin(admin.ModelAdmin):
    form = MediaForm
    list_display = ('name', 'display_image')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"/>')

    display_image.short_description = 'Aperçu'


admin.site.register(Media, MediaAdmin)

# Register the admin interface for the models
admin.site.register(Announcement)
admin.site.register(Room)
admin.site.register(Teacher)
admin.site.register(Time)
admin.site.register(Configuration)
admin.site.register(Planning)
