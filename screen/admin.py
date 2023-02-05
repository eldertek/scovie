from django.contrib import admin
from django.urls import path
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .forms import MediaForm
from .models import (Announcement, Configuration, Media, Planning, Room,
                     Teacher, Time)


# Admin interface for the announcements
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['type', 'message']
    list_editable = ['message']
    list_display_links = None

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        if obj.type in [_('Retards'), _('Absences'), _('Remplacements'), _('Informations')]:
            self.message_user(request, _("Cannot delete default type"))
        else:
            obj.delete()


admin.site.register(Announcement, AnnouncementAdmin)


# Admin interface for the teacher
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_editable = ['name']
    list_display_links = None


admin.site.register(Teacher, TeacherAdmin)


# Admin interface for the time
class TimeAdmin(admin.ModelAdmin):
    list_display = ['name', 'rank']
    list_editable = ['name', 'rank']
    list_display_links = None


admin.site.register(Time, TimeAdmin)


# Admin interface for the room
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_editable = ['name']
    list_display_links = None


admin.site.register(Room, RoomAdmin)


# Admin interface for thhe configurations
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    list_editable = ['value']
    list_display_links = None

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        self.message_user(request, _("Cannot delete default configuration"))


admin.site.register(Configuration, ConfigurationAdmin)


# Admin interface for the medias
class MediaAdmin(admin.ModelAdmin):
    form = MediaForm
    list_display = ('name', 'display_image')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"/>')

    display_image.short_description = _('Preview')


admin.site.register(Media, MediaAdmin)

# Register the admin interface for the models
admin.site.register(Planning)
