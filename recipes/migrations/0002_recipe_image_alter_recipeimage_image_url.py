# Generated by Django 4.2.11 on 2024-04-16 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='recipeimage',
            name='image_url',
            field=models.ImageField(upload_to='photos/%y/%m/%d'),
        ),
    ]
