from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(
        required=False, choices=(("title", "Title"), ("contributor", "Contributor"))
    )


class PublisherForm(forms.Form):
    name = forms.CharField(max_length=50)
    website = forms.URLField()
