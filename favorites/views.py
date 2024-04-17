from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Favorite, Recipe
from recipes.models import RecipeImage, Recipe
from django.shortcuts import render
from django.contrib import messages

@login_required
@require_POST
def add_to_favorite(request, recipe_id):
    # Check if user is authenticated
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        recipe = Recipe.objects.get(pk=recipe_id)

        # Check if recipe is already in favorites
        if Favorite.objects.filter(user=user, Recipe=recipe).exists():
            return JsonResponse({'status': 'error', 'message': 'Recipe is already in favorites'}, status=400)
        
        # Add recipe to favorites
        Favorite.objects.create(user=user, Recipe=recipe)
        return render(request, 'favourite-list.html', {'favorites': Favorite.objects.filter(user=request.user),})
    else:
        # Return error if user is not authenticated
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated'}, status=403)

@login_required
@require_POST
def remove_from_favorite(request, recipe_id):
    # Check if user is authenticated
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        recipe = Recipe.objects.get(pk=recipe_id)

        # Check if recipe is in favorites
        if Favorite.objects.filter(user=user, Recipe=recipe).exists():
            # Remove recipe from favorites
            Favorite.objects.filter(user=user, Recipe=recipe).delete()
            messages.error(request, 'Recipe removed from favorites')
            return JsonResponse({'status': 'success', 'message': 'Recipe removed from favorites'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Recipe is not in favorites'}, status=400)
    else:
        # Return error if user is not authenticated
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated'}, status=403)

def favourite_recipes(request):
    if request.user.is_authenticated:
        favorite_recipes = Favorite.objects.filter(user=request.user)
        images = {}
        for fav in favorite_recipes:
            images[fav.Recipe.id] = RecipeImage.objects.filter(recipe=fav.Recipe)
    else:
        favorite_recipes = []

    return render(request, 'favourite-list.html', {'favorites': favorite_recipes, 'images': images})

