# Generated by Django 4.2.11 on 2024-04-16 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_image_recipe_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image_url',
        ),
    ]