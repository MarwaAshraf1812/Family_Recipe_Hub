from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeImage, RecipeIngredient, Instruction
from favorites.models import Favorite
from django.http import JsonResponse



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
    # Render the template with the top recipes
    return render(request, 'recipes/home.html', {'top_recipes': top_recipes})


def recipes(request):
    recipes = Recipe.objects.all()
    fav = []
    if request.user.is_authenticated:
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


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    instructions = Instruction.objects.filter(recipe=recipe)
    images = RecipeImage.objects.filter(recipe=recipe)
    # categories = recipe.category_set.all()  # Retrieve categories associated with the recipe

    recipe_data = {
        'id': recipe.id,
        'title': recipe.title,
        # 'categories': categories,
        'description': recipe.description,
        'prep_time': recipe.prep_time,
        'cook_time': recipe.cook_time,
        'cuisine': recipe.cuisine,
        'avg_rating': float(recipe.avg_rating) if recipe.avg_rating else None,
        'ingredients': ingredients,
        'instructions': instructions,
        'images': images,
    }

    return render(request, 'recipes/recipe.html', {'recipe_data': recipe_data})

def recipe_search(request):
    query = request.GET.get('query', '')
    if query:
        # Query the database for recipes matching the search query
        search_results = Recipe.objects.filter(title__icontains=query).values('id', 'title')
        return render(request, 'recipes/recipe.html', {'search_results': search_results})
    else:
        return JsonResponse([], safe=False)
