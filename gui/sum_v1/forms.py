from django import forms

from .models import File_upload


class File_uploadForm(forms.ModelForm):
    class Meta:
        model = File_upload
        fields = ('file','sum_words',)
