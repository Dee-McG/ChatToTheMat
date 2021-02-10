from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PrivateMessages(models.Model):
    """
    A model for sending and receiving private messages
    """
    from_user = models.CharField(max_length=80,
                            null=False, blank=False)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(max_length=80,
                            null=False, blank=False)
    message = models.CharField(max_length=1500,
                            null=False, blank=False)

    def __str__(self):
        return self.from_user or ''