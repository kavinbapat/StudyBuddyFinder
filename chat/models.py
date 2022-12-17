from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class Room(models.Model):
    """Represents chat rooms that users can join"""
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=500)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name
