from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeImage, RecipeIngredient, Category, Ingredient, Instruction


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe.html', {'recipe': recipe})


def recipes(request):
    return render(request, 'recipes/recipes.html', {'recipes': Recipe.objects.all(), 'recipeimage': RecipeImage.objects.all()})
