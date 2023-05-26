from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Media, Planning, Room, Teacher, Time


class PlanningForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=Teacher.objects.all(), required=True, label=(_("teacher")).capitalize())
    time = forms.ModelChoiceField(queryset=Time.objects.all(), required=True, label=(_("time")).capitalize())
    room = forms.ModelChoiceField(queryset=Room.objects.all(), required=True, label=(_("room")).capitalize())

    class Meta:
        model = Planning
        fields = ['teacher', 'time', 'room']


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'image']

    def clean(self):
        if Media.objects.count() >= 3:
            raise forms.ValidationError(
                _("You have reached the maximum number of images"))
        return self.cleaned_data
