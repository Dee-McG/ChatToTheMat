from django.db import models


CONTACT_CHOICES = (
    ('breach_of_tos', 'BREACH OF TOS'),
    ('general_query', 'GENERAL QUERY'),
    ('technical_issue', 'TECHNICAL ISSUE'),
    ('subscription_query', 'SUBSCRIPTION QUERY'),
)


class Contact(models.Model):
    """
    A Contact model for staff to view users queries
    """
    contact_reason = models.CharField(max_length=100,
                                      choices=CONTACT_CHOICES,
                                      default='general_query',
                                      null=False, blank=False)
    name = models.CharField(max_length=80,
                            null=False, blank=False)
    email = models.CharField(max_length=80,
                             null=True, blank=True)
    comments = models.CharField(max_length=1500, null=False, blank=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
