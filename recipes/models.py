from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    cuisine = models.CharField(max_length=100)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    difficulty = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.name}"

class Instruction(models.Model):
    """"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.recipe.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='photos/%y/%m/%d')

    def __str__(self):
        return self.recipe.title

# Create your models here.
