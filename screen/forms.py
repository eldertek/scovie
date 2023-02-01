from .models import Media
from django import forms


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'image']

    def clean(self):
        if Media.objects.count() >= 6:
            raise forms.ValidationError("Vous avez atteint le nombre maximum d'images")
        return self.cleaned_data