from django.contrib.auth.models import Group, Permission, User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username
