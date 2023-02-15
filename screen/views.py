from django.shortcuts import render
from .models import Announcement, Configuration, Planning, Room, Time, Media
import datetime

config = Configuration.get_solo

def index(request):
    # Create a context
    context = {}
    # Get emergency status from configuration
    emergency_mode = config.emergency_mode
    # If emergency status is True
    if emergency_mode == 'True':
        # Force screen mode to emergency
        screen_mode = 'emergency'
        # Clean screen modes with only emergency
        screen_modes = ['emergency']
        mobile_screen_modes = ['emergency']
        # Emergency context
        emergency_context = {
            'emergency_title': config.emergency_title,
            'emergency_subtitle': config.emergency_subtitle,
        }
        # Update context with emergency context
        context.update(emergency_context)
    else:
        # Get screen mode from GET request, default to all
        screen_mode = request.GET.get('screen_mode', 'all')
        # Available screen modes
        screen_modes = ['all', 'informations', 'caroussel']
        mobile_screen_modes = ['informations']
        # Saint-Valentine day feature
        if datetime.datetime.now().month == 2 and datetime.datetime.now().day == 14:
            screen_modes.append('valentine')

    temp = {
        'enterprise_name': config.enterprise_name,
        'planning': Planning.objects.all(),
        'rooms':  Room.objects.filter(planning__teacher__isnull=False).distinct(),
        'announcements': Announcement.objects.all(),
        'times': Time.objects.all(),
        'medias': Media.objects.all(),
        'mobile_screen_modes': mobile_screen_modes,
        'screen_modes': screen_modes,
        'screen_mode': screen_mode,
    }

    context.update(temp)

    return render(request, 'index.html', context)
