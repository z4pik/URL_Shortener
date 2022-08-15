from .models import ShortUrl
from django import forms


class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = {'original_url'}

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }
