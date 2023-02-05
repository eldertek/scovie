from .models import Media
from django import forms


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'image']

    def clean(self):
        if Media.objects.count() >= 6:
            raise forms.ValidationError(_("You have reached the maximum number of images"))
        return self.cleaned_data