from django import forms
from .models import DocumentForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentForm
        fields = ('description', 'photo', 'filters')


# class UploadForm(forms.Form):
#     image = forms.ImageField()
#     description = forms.CharField()
