from django.shortcuts import render
from django.http import JsonResponse
from .models import Announcement, Configuration, Planning, Room, Time, Media
import datetime
import locale

def index(request):
    # Create a context
    context = {}
    # Get emergency status from configuration
    emergency_status = Configuration.get_value('emergency_status')
    # If emergency status is True
    if emergency_status == 'True':
        # Force screen mode to emergency
        screen_mode = 'emergency'
        # Clean screen modes with only emergency
        screen_modes = ['emergency']
        # Emergency context
        emergency_context = {
            'emergency_title': Configuration.get_value('emergency_title'),
            'emergency_subtitle': Configuration.get_value('emergency_subtitle')
        }
        # Update context with emergency context
        context.update(emergency_context)
    else:
        # Default screen mode
        screen_mode = 'all'
        # Available screen modes
        screen_modes = ['all', 'informations', 'caroussel']
        # Saint-Valentine day feature
        if datetime.datetime.now().month == 2 and datetime.datetime.now().day == 3:
            screen_modes.append('valentine')

    temp = {
        'retards': Announcement.objects.filter(type='RETARD'),
        'absences': Announcement.objects.filter(type='ABSENCE'),
        'remplacements': Announcement.objects.filter(type='REMPLACEMENT'),
        'informations': Announcement.objects.filter(type='INFORMATION'),
        'enterprise_name': Configuration.get_value('enterprise_name'),
        'planning': Planning.objects.all(),
        'rooms': Room.objects.filter(planning__teacher__isnull=False),
        'times': Time.objects.all(),
        'medias': Media.objects.all(),
        'screen_modes': screen_modes,
        'screen_mode': screen_mode
    }

    context.update(temp)

    return render(request, 'index.html', context)
