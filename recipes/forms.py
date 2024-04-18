# forms.py

from django import forms

class RecipeSearchForm(forms.Form):
    search_query = forms.CharField(label='Search')
