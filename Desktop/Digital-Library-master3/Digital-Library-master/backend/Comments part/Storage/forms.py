from .models import Tag
from django import forms


DISPLAY_CHOICES = list()
for el in tuple(Tag.objects.values_list('name', flat=True)):
    DISPLAY_CHOICES.append((el, el))


class UploadForm(forms.Form):
    search_for = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "search-field"
            }
        )
    )
    tags_passed = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': "tag-checkbox"}),
        choices=DISPLAY_CHOICES,
    )
    date_passed = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            attrs={
                'class': "date-field"}
        ),
    )
