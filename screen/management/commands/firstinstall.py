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
        # Delete environment file
        self.stdout.write(self.style.MIGRATE_HEADING(
            'Deleting environment file...'))
        if os.path.isfile('scovie/environment.py'):
            os.remove('scovie/environment.py')

        # Create environment file
        self.stdout.write(self.style.MIGRATE_HEADING(
            'Creating environment file...'))
        with open('scovie/environment.py', 'w') as f:
            f.write('# CONFIGURATION VARIABLES\n')
        # Ask for language
        language_code = input(self.style.NOTICE(
            'What language do you prefer? (fr/en) ? '))
        if language_code not in ['fr', 'en']:
            raise CommandError(
                'Invalid language code. Please enter either "fr" or "en".')
        # Write LANGUAGE_CODE in environment file
        with open('scovie/environment.py', 'a') as f:
            f.write(f'LANGUAGE_CODE = "{language_code}"\n')
        # Activate the language
        activate(language_code)
        from django.utils.translation import gettext_lazy as _
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Generating secret key...')))
        # Generate a new SECRET_KEY
        secret_key = secrets.token_hex(24)
        # Write SECRET_KEY in environment file
        with open('scovie/environment.py', 'a') as f:
            f.write(f'SECRET_KEY = "{secret_key}"\n')

        # Write DEBUG in environment file
        with open('scovie/environment.py', 'a') as f:
            f.write(f'DEBUG = "False"\n')

        # Write ALLOWED_HOSTS in environment file
        with open('scovie/environment.py', 'a') as f:
            f.write(f'ALLOWED_HOSTS = []\n')

        # Clear database
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Cleaning up database...')))
        os.system('python manage.py flush --no-input')
        # Make migrations
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Running makemigrations...')))
        os.system('python manage.py makemigrations')
        # Migrate
        self.stdout.write(self.style.MIGRATE_HEADING(_('Running migrate...')))
        os.system('python manage.py migrate')
        # Create default announcement types (absences, remplacements, retards, informations)
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Creating default announcement types...')))
        Announcement.objects.create(
            type=_("Absences"), message=_("No absences"))
        Announcement.objects.create(
            type=_("Replacements"), message=_("No replacements"))
        Announcement.objects.create(type=_("Delays"), message=_("No delays"))
        Announcement.objects.create(
            type=_("Informations"), message=_("No informations"))
        # Create configuration default values
        enterprise_name = input(self.style.NOTICE(
            _('What is the name of your enterprise ? ')))
        Configuration.objects.create(
            name="enterprise_name", value=str(enterprise_name))
        Configuration.objects.create(name="emergency_status", value=False)
        Configuration.objects.create(
            name="emergency_title", value=_("Emergency mode ON !"))
        Configuration.objects.create(name="emergency_subtitle", value=_(
            "Please follow security instructions"))
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
        # Create superuser
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Running createsuperuser...')))
        os.system('python manage.py createsuperuser')
