from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, Instruction, RecipeImage, Category


admin.site.register(Recipe)
admin.site.register(Instruction)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeImage)
admin.site.register(Category)
# Register your models here.
