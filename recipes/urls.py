from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.recipes, name='recipes'),

    path('recipe/', views.recipe, name='recipe')

=======
    path('recipes/', views.recipes, name='recipes'),
    path('', views.home, name='home'),
    path('recipe', views.recipe, name='recipe')
>>>>>>> 17a097ace3438f8d7f35f1c4a5c1c45395dd2c0c
]
