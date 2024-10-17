from django import forms
from django.core.exceptions import ValidationError
from .models import Publisher, Review


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(
        required=False, choices=(("title", "Title"), ("contributor", "Contributor"))
    )


# class PublisherForm(forms.Form):
#     name = forms.CharField(max_length=50, help_text="The name of the Publisher.")
#     website = forms.URLField(help_text="The Publisher's website.")
#     email = forms.EmailField(help_text="The Publisher's email address.")


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)