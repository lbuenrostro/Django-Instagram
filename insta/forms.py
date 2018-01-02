from django import forms
from .models import DocumentForm
from PIL import Image, ImageFilter


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentForm
        fields = ('description', 'photo')


class FiltersForm(forms.Form):
    choices = [
        ('', ''),
        ('broken_glass', 'Broken Glass'),
        ('convert_grayscale', 'Grey'),
        ('BLUR', 'Blur'),
        ('CONTOUR', 'Contour'),
        ('DETAIL', 'Detail'),
        ('EDGE_ENHANCE_MORE', 'Extra Edge-Enhance'),
        ('EMBOSS', 'Emboss'),
        ('FIND_EDGES', 'Find Edges'),
        ('SMOOTH', 'Smooth'),
        ('SMOOTH_MORE', 'Extra Smooth'),
        ('SHARPEN', 'Sharpen'),
    ]
    filters = forms.ChoiceField(choices=choices)

    def apply_filter(self):
        return {
            'Broken Glass': broken_glass,
            'Grey': convert_grayscale,
            'BLUR': ImageFilter.GaussianBlur(2),
            'CONTOUR': ImageFilter.CONTOUR,
            'EMBOSS': ImageFilter.EMBOSS,
            'DETAIL': ImageFilter.DETAIL,
            'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
            'FIND_EDGES': ImageFilter.FIND_EDGES,
            'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
            'SHARPEN': ImageFilter.SHARPEN,
        }.get(self.cleaned_data['filters'], None)