from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model to save or edit user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80,
                            null=True, blank=True)
    location = models.CharField(max_length=80,
                                null=True, blank=True)
    bio = models.CharField(max_length=1500,
                           null=True, blank=True)
    img_url = models.CharField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return self.name or ''
