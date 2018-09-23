from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('text_input','document','directory',)
        widgets = {
            'text_input': forms.Textarea(attrs={'rows': 15, 'cols': 120})
        }
        