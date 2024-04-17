# forms.py in your recipes app
from django import forms
from .models import Recipe, Ingredient, Instruction, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'  # Use all fields from the Recipe model
        
class RecipeSearchForm(forms.Form):
    SearchRequest = forms.CharField(initial='Search Recipe', max_length=100)
