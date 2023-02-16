from django.contrib import admin, messages
from solo.admin import SingletonModelAdmin
from django.shortcuts import redirect
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
        if obj.type in [_('Absences'), _('Remplacements'), _('Informations')]:
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
admin.site.register(Configuration, SingletonModelAdmin)


# Admin interface for the medias
class MediaAdmin(admin.ModelAdmin):
    form = MediaForm
    list_display = ('name', 'display_image')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"/>')

    display_image.short_description = _('Preview')


admin.site.register(Media, MediaAdmin)


# Admin interface for the planning
class PlanningAdmin(admin.ModelAdmin):
    list_display = ('room', 'time', 'teacher')
    change_list_template = 'admin/planning_change_list.html'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        actions['delete_all'] = (self.delete_all, 'delete_all', (_("Delete all")))
        return actions

    def delete_all(self, request, queryset):
        queryset.delete()
        messages.success(request, (_("All items have been deleted.")))
        return redirect("admin:screen_planning_changelist")

    def changelist_view(self, request, extra_context=None):
        if request.POST.get('action') == 'delete_all':
            queryset = self.model.objects.all()
            return self.delete_all(request, queryset)
        extra_context = extra_context or {}
        planning = self.model.objects.all()
        times = Time.objects.all()
        rooms = Room.objects.all()
        extra_context['rooms'] = rooms
        extra_context['times'] = times
        extra_context['planning'] = planning
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Planning, PlanningAdmin)
