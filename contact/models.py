from django.db import models


class Contact(models.Model):
    """
    A Contact model for staff to view users queries
    """
    contact_reason = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=80,
                            null=False, blank=False)
    email = models.CharField(max_length=80,
                             null=True, blank=True)
    comments = models.CharField(max_length=1500, null=False, blank=False)

    def __str__(self):
        return self.name
