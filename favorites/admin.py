from django.contrib import admin

# Register your models here.
from .models import Favorite

admin.site.register(Favorite)