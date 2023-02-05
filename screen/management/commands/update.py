import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext_lazy as _

from screen.models import (Announcement, Configuration, Media, Planning, Room,
                           Teacher, Time)


class Command(BaseCommand):
    help = _('Runs an update of scovie, be cautious !')

    def handle(self, *args, **options):
        # If system is not linux, raise an error
        if os.name != 'posix' or os.name != 'linux':
            raise CommandError('This command is only available on linux')
        else: 
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Creating backup...')))
            # Save current directory in backup_dir
            backup_dir = os.getcwd()
            # Copy all files in a backup directory
            os.system(f'cp -r {backup_dir} {backup_dir}/backup')
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Updating scovie...')))
            # Pull the latest changes from the github repository
            os.system('git pull')
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(
                _('Running makemigrations...')))
            # Make migrations
            os.system('python manage.py makemigrations')
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Running migrate...')))
            # Migrate
            os.system('python manage.py migrate')
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Scovie updated !')))
