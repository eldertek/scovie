import base64
import datetime
import os
import re

from django.core.exceptions import ValidationError
from django.db import models


# Functions
def format_filename(instance, filename):
    date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    name, extension = filename.rsplit('.', 1)
    name = re.sub(r'\W+', '', name)
    return os.path.join('static/uploads/', f"{date}-{name}.{extension}")


# Models
class Announcement(models.Model):
    class Meta:
        verbose_name = "annonce"
        ordering = ['type']


    TYPE_CHOICES = (
        ('RETARD', 'Retard'),
        ('ABSENCE', 'Absence'),
        ('REMPLACEMENT', 'Remplacement'),
        ('INFORMATION', 'Information'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    text = models.TextField()

    def __str__(self):
        return self.type + " : " + self.text


class Room(models.Model):
    class Meta:
        verbose_name = "salle"
        ordering = ['name']

    name = models.CharField(max_length=5)

    @classmethod
    def get_occupied_rooms(cls):
        return cls.objects.filter(planning__teacher__isnull=False).distinct()

    def __str__(self):
        return self.name


class Teacher(models.Model):    
    class Meta:
        verbose_name = "enseignant"
        ordering = ['name']

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Time(models.Model):
    class Meta:
        verbose_name = "période"
        ordering = ['rank']

    name = models.CharField(max_length=5)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Planning(models.Model):
    class Meta:
        verbose_name = "planning"

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return 'Planning pour ' + self.time.name + ' en ' + self.room.name + ' avec ' + self.teacher.name


class Configuration(models.Model):
    class Meta:
        verbose_name = "paramètre"

    name = models.CharField(max_length=30)
    value = models.TextField()

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
        verbose_name = "média"

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=format_filename)
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return "Image: " + self.name
