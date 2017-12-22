from django import forms
from .models import DocumentForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentForm
        fields = ('description', 'photo')