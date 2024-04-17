from django.urls import path
from .views import add_to_favorite, remove_from_favorite, favourite_recipes

app_name = 'favorites'

urlpatterns = [
    path('favourite_list/', favourite_recipes, name='favourite_recipes'),
    path('add/<int:recipe_id>/', add_to_favorite, name='add_to_favorite'),
    path('remove/<int:recipe_id>/', remove_from_favorite, name='remove_from_favorite'),
]
