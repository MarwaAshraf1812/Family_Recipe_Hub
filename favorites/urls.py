from django.urls import path
from .views import add_to_favorite, remove_from_favorite

app_name = 'favorites'

urlpatterns = [
    path('add/', add_to_favorite, name='add_to_favorite'),
    path('remove/', remove_from_favorite, name='remove_from_favorite'),
]
