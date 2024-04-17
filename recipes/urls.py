from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('', views.home, name='home'),
    path('recipe', views.recipe_details, name='recipe'),

]
