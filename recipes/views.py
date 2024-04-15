from django.shortcuts import render

from django.shortcuts import render
from .models import Recipe, RecipeImage, RecipeIngredient, Category, Ingredient, Instruction

def recipe(request):
    return render(request, 'recipes/recipe.html')

# def home(request):
#     return render(request, 'recipes/home.html', {'recipes':Recipe.objects.all()})


from django.shortcuts import render
from recipes.models import Recipe

def home(request):
    # Retrieve all recipes with an average rating greater than 4.5
    top_recipes = Recipe.objects.filter(avg_rating__gt=4.5)

    # Convert avg_rating to float to avoid template filter issue
    top_recipes = [
        {
            'title': recipe.title,
            'avg_rating': float(recipe.avg_rating),
            'images': recipe.recipeimage_set.all()  # Retrieve associated images
        }
        for recipe in top_recipes
    ]
    print(top_recipes)
    # Render the template with the top recipes
    return render(request, 'recipes/home.html', {'top_recipes': top_recipes})



def recipes(request):
    return render(request, 'recipes/recipes.html')


