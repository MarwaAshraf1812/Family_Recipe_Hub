from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Favorite, Recipe

@login_required
@require_POST
def add_to_favorite(request, recipe_id):
    # Check if user is authenticated
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        recipe = Recipe.objects.get(pk=recipe_id)

        # Check if recipe is already in favorites
        if Favorite.objects.filter(user=user, recipe=recipe).exists():
            return JsonResponse({'status': 'error', 'message': 'Recipe is already in favorites'}, status=400)
        
        # Add recipe to favorites
        favorite, created = Favorite.objects.create(user=user, recipe=recipe)
        return JsonResponse({'status': 'success', 'message': 'Recipe added to favorites'}, status=200)
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
        if Favorite.objects.filter(user=user, recipe=recipe).exists():
            # Remove recipe from favorites
            Favorite.objects.filter(user=user, recipe=recipe).delete()
            return JsonResponse({'status': 'success', 'message': 'Recipe removed from favorites'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Recipe is not in favorites'}, status=400)
    else:
        # Return error if user is not authenticated
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated'}, status=403)

