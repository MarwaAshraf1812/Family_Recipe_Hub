from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),

    path('recipe', views.recipe, name='recipe')

]
