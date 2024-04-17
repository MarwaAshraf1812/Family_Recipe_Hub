from django.shortcuts import render
from .models import Recipe, RecipeImage, RecipeIngredient, Category, Ingredient, Instruction
from django.conf import settings
from favorites.models import Favorite

def recipe(request):
    return render(request, 'recipes/recipe.html') 

# def home(request):
#     return render(request, 'recipes/home.html', {'recipes':Recipe.objects.all()})


def home(request):
    # Retrieve all recipes with an average rating greater than 4.5
    top_recipes = Recipe.objects.filter(avg_rating__gt=4.5)

    # Convert avg_rating to float to avoid template filter issue
    top_recipes = [
        {
            'title': recipe.title,
            'avg_rating': float(recipe.avg_rating),
            # Filter image depends on recipe id
            'images': RecipeImage.objects.filter(recipe=recipe)
        }
        for recipe in top_recipes
    ]
    print(top_recipes)
    # Render the template with the top recipes
    return render(request, 'recipes/home.html',{'top_recipes': top_recipes})



def recipes(request):
    recipes = Recipe.objects.all()
    favorite_recipes = Favorite.objects.filter(user=request.user)
    fav = [recipe.Recipe.id for recipe in favorite_recipes]
    recipesData = [{
        'id': recipe.id,
        'title': recipe.title,
        'avg_rating': float(recipe.avg_rating),
        'images':  RecipeImage.objects.filter(recipe=recipe),
    }
    for recipe in recipes
    ]
    return render(request, 'recipes/recipes.html', {'recipes': recipesData, 'favorites': fav})

def recipe_search(request):
    if request.method == 'POST':
        form = RecipeSearchForm(request.POST)
        if form.is_valid():
            search_request = form.cleaned_data['SearchRequest']
            # Perform the search query
            results = Recipe.objects.filter(
                Q(title__icontains=search_request) |  # Title contains the search_request
                Q(recipeingredient__ingredient__name__icontains=search_request)  # Ingredient name contains the search_request
            ).distinct()  # Use distinct to avoid duplicate results
            return render(request, 'search_results.html', {'results': results, 'search_request': search_request})
    else:
        form = RecipeSearchForm()
    return render(request, 'search_form.html', {'form': form})
