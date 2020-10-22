from .models import Tag
from django import forms


DISPLAY_CHOICES = list()
for el in tuple(Tag.objects.values_list('name', flat=True)):
    DISPLAY_CHOICES.append((el, el))


class UploadForm(forms.Form):
    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': "filter-checkbox"}),
        choices=DISPLAY_CHOICES,
    )
