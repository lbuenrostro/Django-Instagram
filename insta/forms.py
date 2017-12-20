from django import forms
from uploads.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'photo')


# class UploadFileFrom(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()