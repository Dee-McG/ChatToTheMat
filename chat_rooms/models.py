from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    """
    A model to save and display chat messages
    """
    user = models.CharField(max_length=80,
                            null=True, blank=True)
    message = models.CharField(max_length=500,
                            null=False, blank=False)
    time = models.DateTimeField(max_length=80,
                            null=True, blank=True)

    def __str__(self):
        return self.user