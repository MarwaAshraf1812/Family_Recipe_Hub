from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),

    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe')

]
