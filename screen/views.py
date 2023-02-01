from django.shortcuts import render
from django.http import JsonResponse
from .models import Announcement, Configuration, Planning, Room, Time, Media
import datetime, locale

def general_context(request):
    return {
        'enterprise_name': Configuration.get_value('enterprise_name'),
    }

def informations_context(request):
    announcements = Announcement.objects.all()
    planning = Planning.objects.all()
    rooms = Room.get_occupied_rooms()
    times = Time.objects.all()

    return {
        'announcements': announcements,
        'planning': planning,
        'rooms': rooms,
        'times': times,
    }

def caroussel_context(request):
    return {
        'medias': Media.objects.all(),
    }

def index(request):
    today = datetime.date.today()
    if today.month == 2 and today.day == 14:
        events = 'screen/events/valentine'
    else:
        events = None
    return render(request, 'index.html', { 'events': events })

def informations(request):
    return render(request, 'pages/informations.html', {**general_context(request), **informations_context(request)})

def caroussel(request):
    return render(request, 'pages/caroussel.html', {**general_context(request), **caroussel_context(request)})

def all(request):
    return render(request, 'pages/all.html', {**general_context(request), **informations_context(request), **caroussel_context(request)})
        
def valentine(request):
    return render(request, 'events/valentine.html', {**general_context(request)})