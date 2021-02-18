from django.db import models
from django.contrib.auth.models import User


class BannedUsers(models.Model):
    """
    A model to ban users to prevent them posting in chat rooms
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    banned = models.BooleanField(default=False)
    reason = models.CharField(max_length=500,
                              null=False, blank=False)

    def __str__(self):
        return self.reason
