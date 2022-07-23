from django import forms
from .models import Learning


class LearningForm(forms.ModelForm):

    class Meta:
        model = Learning
        fields = ['title', 'subtitle', 'link']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title'
            }),
            'subtitle': forms.TextInput(attrs={
                'placeholder': 'Subtitle'
            }),
            'link': forms.URLInput(attrs={
                'placeholder': 'Source'
            })
        }

    def clean_title(self):
        return self.cleaned_data['title'].upper()

    def clean_subtitle(self):
        return self.cleaned_data['subtitle'].upper()
