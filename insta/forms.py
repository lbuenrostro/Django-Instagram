from django import forms
from .models import DocumentForm
from PIL import Image, ImageFilter


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentForm
        fields = ('description', 'photo')


class FiltersForm(forms.Form):
    filters_choice = [('', ''), ('BLUR', 'BLUR'), ('CONTOUR', 'CONTOUR'),
                      ('DETAIL', 'DETAIL'), ('EDGE_ENHANCE', 'EDGE_ENHANCE'),
                      ('EDGE_ENHANCE_MORE', 'EDGE_ENHANCE_MORE'), ('EMBOSS',
                                                                   'EMBOSS'),
                      ('FIND_EDGES', 'FIND_EDGES'), ('SMOOTH', 'SMOOTH'),
                      ('SMOOTH_MORE', 'SMOOTH_MORE'), ('SHARPEN', 'SHARPEN')]
    filters = forms.ChoiceField(choices=filters_choice)

    def apply_filter(self):
        return {
            'BLUR': ImageFilter.BLUR,
            'CONTOUR': ImageFilter.CONTOUR,
            'DETAIL': ImageFilter.DETAIL,
            'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
            'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
            'EMBOSS': ImageFilter.EMBOSS,
            'FIND_EDGES': ImageFilter.FIND_EDGES,
            'SMOOTH': ImageFilter.SMOOTH,
            'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
            'SHARPEN': ImageFilter.SHARPEN
        }.get(self.cleaned_data['filters'], None)