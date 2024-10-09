# from django import forms


# class SearchForm(forms.Form):
#     CHOICE_LIST = (("title", "Title"), ("contributor", "Contributor"))
#     search = forms.CharField(required=False, min_length=3)
#     search_in = forms.ChoiceField(choices=CHOICE_LIST, required=False)

from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(
        required=False, choices=(("title", "Title"), ("contributor", "Contributor"))
    )
