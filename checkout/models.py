from django.db import models
from django.contrib.auth.models import User
from stripe.api_resources import subscription


# Create your models here.
class PremiumUser(models.Model):
    """
    A model to record subscription members
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(max_length=80,
                            null=False, blank=False)
    end_date = models.DateTimeField(max_length=80,
                            null=False, blank=False)
    subscription = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username