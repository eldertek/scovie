import os
import secrets

from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import activate
from django.utils.translation import gettext_lazy as _

from screen.models import (Announcement, Configuration, Media, Planning, Room,
                           Teacher, Time)


class Command(BaseCommand):
    help = _(
        'Runs first install commands, be cautious ! This will delete all data in database !')

    def handle(self, *args, **options):
        # Get config
        config = Configuration.get_solo()
        # Create default announcement types (absences, remplacements, informations)
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Creating default announcement types...')))
        Announcement.objects.create(
            type=_("Absences"), message=_("No absences"))
        Announcement.objects.create(
            type=_("Replacements"), message=_("No replacements"))
        Announcement.objects.create(
            type=_("Informations"), message=_("No informations"))
        # Create configuration default values
        enterprise_name = input(self.style.NOTICE(
            _('What is the name of your enterprise ? ')))
        config.enterprise_name = enterprise_name
        config.emergency_mode = False
        config.emergency_title = _("Emergency mode ON !")
        config.emergency_subtitle = _("Please follow security instructions")
        # Save configuration
        config.save()
        # Create time defaults
        Time.objects.create(name="M1", rank=1)
        Time.objects.create(name="M2", rank=2)
        Time.objects.create(name="M3", rank=3)
        Time.objects.create(name="M4", rank=4)
        Time.objects.create(name="S1", rank=5)
        Time.objects.create(name="S2", rank=6)
        Time.objects.create(name="S3", rank=7)
        Time.objects.create(name="S4", rank=8)
        # Create planning defaults, teacher, room
        Room.objects.create(name=_("Room 1"))
        room = Room.objects.get(name=_("Room 1"))
        Teacher.objects.create(name=_("Teacher 1"))
        teacher = Teacher.objects.get(name=_("Teacher 1"))
        Planning.objects.create(
            room=room, time=Time.objects.get(name="M1"), teacher=teacher)
        # Create media defaults
        Media.objects.create(
            name=_("Image 1"), image="static/uploads/image1.jpg")