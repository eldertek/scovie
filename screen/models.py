import datetime
import os
import re

from django.db import models
from django.utils.translation import gettext_lazy as _


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

    name = models.CharField(max_length=15, verbose_name=_("teacher"))

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


class Configuration(models.Model):
    class Meta:
        verbose_name = _("parameter")

    name = models.CharField(max_length=30, unique=True, verbose_name=_("parameter"))
    value = models.CharField(max_length=90, verbose_name=_("value"))

    @classmethod
    def get_value(cls, name):
        try:
            return cls.objects.get(name=name).value
        except cls.DoesNotExist:
            return None

    def __str__(self):
        return self.name + ' = ' + self.value


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
