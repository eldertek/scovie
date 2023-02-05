import os
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext_lazy as _

from screen.models import (Announcement, Configuration, Media, Planning, Room,
                           Teacher, Time)


class Command(BaseCommand):
    help = _('Runs an update of scovie, be cautious !')

    def handle(self, *args, **options):
        # If system is linux
        if os.name == 'posix':
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
            self.stdout.write(self.style.MIGRATE_HEADING(_('Running makemigrations...')))
            # Make migrations
            os.system('python3 manage.py makemigrations')
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Running migrate...')))
            # Migrate
            os.system('python3 manage.py migrate')
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Scovie updated !')))
        else: 
            # Print a message to the user
            self.stdout.write(self.style.MIGRATE_HEADING(_('Scovie can only be updated on a linux system !')))