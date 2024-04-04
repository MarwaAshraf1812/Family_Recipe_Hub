from django.shortcuts import render

from django.shortcuts import render
from .models import Recipe, RecipeImage, RecipeIngredient, Category, Ingredient, Instruction

def recipe(request):
    return render(request, 'recipes/recipe.html')

def recipes(request):
    return render(request, 'recipes/recipes.html', {'recipes':Recipe.objects.all(), 'recipeimage': RecipeImage.objects.all()})


