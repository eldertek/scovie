from django.shortcuts import render
from django.http import JsonResponse
from .models import Announcement, Configuration, Planning, Room, Time, Media
import datetime
import locale


def index(request):
    # Default screen mode
    screen_mode = 'all'
    # Available screen modes
    screen_modes = ['all', 'informations', 'caroussel']

    # If we are valentine's day append valentine
    if datetime.datetime.now().month == 2 and datetime.datetime.now().day == 3:
        screen_modes.append('valentine')

    # Check if a new screen mode has been requested
    if request.GET.get('screen_mode'):
        screen_mode = request.GET['screen_mode']

    context = {
        'announcements': Announcement.objects.all(),
        'enterprise_name': Configuration.get_value('enterprise_name'),
        'planning': Planning.objects.all(),
        'rooms': Room.objects.all(),
        'times': Time.objects.all(),
        'medias': Media.objects.all(),
        'screen_modes': screen_modes,
        'screen_mode': screen_mode
    }

    return render(request, 'index.html', context)
