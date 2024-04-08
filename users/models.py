from django.contrib.auth.models import AbstractUser
from django.db import models
from recipes.models import Recipe

class Users(AbstractUser):
    full_name = models.CharField(max_length=255)  # Add field for full name
    email = models.EmailField(unique=True)  # Add field for email
    join_date = models.DateTimeField(auto_now_add=True)  # Add field for join date
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='users_custom',
        related_query_name='user_custom'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='users_custom',
        related_query_name='user_custom'
    )

class UserRecipe(models.Model):
    user_custome = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_custome', 'recipe')  # Ensure each recipe is unique per user
