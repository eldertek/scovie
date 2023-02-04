from django.core.management.base import BaseCommand, CommandError
from screen.models import Announcement, Configuration, Planning, Teacher, Room, Time, Media
import os

class Command(BaseCommand):
    help = 'Runs first install commands'

    def handle(self, *args, **options):
        # Clear database
        self.stdout.write(self.style.MIGRATE_HEADING('Cleaning up database...'))
        os.system('python manage.py flush --no-input')
        # Make migrations
        self.stdout.write(self.style.MIGRATE_HEADING('Running makemigrations...'))
        os.system('python manage.py makemigrations')
        # Migrate
        self.stdout.write(self.style.MIGRATE_HEADING('Running migrate...'))
        os.system('python manage.py migrate')
        # Create default announcement types (absences, remplacements, retards, informations)
        self.stdout.write(self.style.MIGRATE_HEADING('Creating default announcement types...'))
        Announcement.objects.create(type="Absences", message="Aucune absence")
        Announcement.objects.create(type="Remplacements", message="Aucun remplacement")
        Announcement.objects.create(type="Retards", message="Aucun retard")
        Announcement.objects.create(type="Informations", message="Aucune information")
        # Create configuration default values
        enterprise_name = input(self.style.NOTICE('What is the name of your enterprise ? '))
        Configuration.objects.create(name="enterprise_name", value=str(enterprise_name))
        Configuration.objects.create(name="emergency_status", value=False)
        Configuration.objects.create(name="emergency_title", value="Emergency mode ON !")
        Configuration.objects.create(name="emergency_subtitle", value="Please follow security instructions")
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
        room, _ = Room.objects.get_or_create(defaults={'name': "Salle 1"})
        teacher, _ = Teacher.objects.get_or_create(defaults={'name': "Professeur 1"})
        Planning.objects.create(room=room, time=Time.objects.get(name="M1"), teacher=teacher)
        # Create media defaults
        Media.objects.create(name="Image 1", image="static/uploads/image1.jpg")
        # Create superuser
        self.stdout.write(self.style.MIGRATE_HEADING('Running createsuperuser...'))
        os.system('python manage.py createsuperuser')
