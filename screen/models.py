import datetime
import os
import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


# Functions
def format_filename(instance, filename):
    date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    name, extension = filename.rsplit('.', 1)
    name = re.sub(r'\W+', '', name)
    return os.path.join('static/uploads/', f"{date}-{name}.{extension}")


# Models
class Announcement(models.Model):
    class Meta:
        verbose_name = _("announcement")
        ordering = ['type']

    type = models.CharField(max_length=20, unique=True, verbose_name=_("type"))
    message = models.TextField(verbose_name=_("message"))

    def __str__(self):
        return self.type + " : " + self.message


class Room(models.Model):
    class Meta:
        verbose_name = _("room")
        ordering = ['name']

    name = models.CharField(max_length=15, verbose_name=_("room"))

    @classmethod
    def get_occupied_rooms(cls):
        return cls.objects.filter(planning__teacher__isnull=False).distinct()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class Meta:
        verbose_name = _("teacher")
        ordering = ['name']

    name = models.CharField(max_length=50, verbose_name=_("teacher"))

    def __str__(self):
        return self.name


class Time(models.Model):
    class Meta:
        verbose_name = _("time")
        ordering = ['rank']

    name = models.CharField(max_length=5, verbose_name=_("time"))
    rank = models.IntegerField(verbose_name=_("display order"))   

    def __str__(self):
        return self.name


class Planning(models.Model):
    class Meta:
        verbose_name = _("planning")
        
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name=_("room"))
    time = models.ForeignKey(Time, on_delete=models.CASCADE, verbose_name=_("time"))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_("teacher"))

    def __str__(self):
         return (_('Planning for {} in {} with {}').format(self.time.name, self.room.name, self.teacher.name))


class Configuration(SingletonModel):
    class Meta:
        verbose_name = _("parameters")


    enterprise_name = models.CharField(max_length=50, verbose_name=_("enterprise name"))

    emergency_mode = models.BooleanField(default=False, verbose_name=_("emergency mode"))
    emergency_title = models.CharField(max_length=50, verbose_name=_("emergency title"))
    emergency_subtitle = models.CharField(max_length=50, verbose_name=_("emergency subtitle"))

    carnival_day = models.BooleanField(default=False, verbose_name=_("carnival day"))
    carnival_date = models.DateField(default=datetime.date(2023, 2, 21,), verbose_name=_("carnival date"))

    valentine_day = models.BooleanField(default=False, verbose_name=_("valentine day"))
    valentine_date = models.DateField(default=datetime.date(2023, 2, 14), verbose_name=_("valentine date"))

    def __str__(self):
        return str(_("Application configuration"))



class Media(models.Model):
    class Meta:
        verbose_name = _("media")

    name = models.CharField(max_length=30, verbose_name=_("name"))
    image = models.ImageField(upload_to=format_filename, verbose_name=_("image"))

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return (_("Image: {}").format(self.name))
