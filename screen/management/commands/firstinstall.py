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
        if os.path.isfile('.env'):
            os.remove('.env')

        # Create environment file
        self.stdout.write(self.style.MIGRATE_HEADING(
            'Creating environment file...'))
        with open('.env', 'w') as f:
            f.write('# CONFIGURATION VARIABLES\n')
        # Ask for language
        language_code = input(self.style.NOTICE(
            'What language do you prefer? (fr/en) ? '))
        if language_code not in ['fr', 'en']:
            raise CommandError(
                'Invalid language code. Please enter either "fr" or "en".')
        # Write LANGUAGE_CODE in environment file
        with open('.env', 'a') as f:
            f.write(f'LANGUAGE_CODE="{language_code}"\n')
        # Activate the language
        activate(language_code)
        from django.utils.translation import gettext_lazy as _
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Generating secret key...')))
        # Generate a new SECRET_KEY
        secret_key = secrets.token_hex(24)
        # Write SECRET_KEY in environment file
        with open('.env', 'a') as f:
            f.write(f'SECRET_KEY="{secret_key}"\n')

        # Write DEBUG in environment file
        with open('.env', 'a') as f:
            f.write(f'DEBUG=False\n')

        # Write ALLOWED_HOSTS in environment file
        with open('.env', 'a') as f:
            f.write(f'ALLOWED_HOSTS="127.0.0.1"\n')

        # Delete database
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Deleting database...')))
        if os.path.isfile('db.sqlite3'):
            os.remove('db.sqlite3')
            
        # Migrate
        self.stdout.write(self.style.MIGRATE_HEADING(_('Running migrate...')))
        os.system('python manage.py migrate')
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
        # Create superuser
        self.stdout.write(self.style.MIGRATE_HEADING(
            _('Running createsuperuser...')))
        os.system('python manage.py createsuperuser')
