from django.contrib import admin
from .models import PremiumUser


class PremiumUserAdmin(admin.ModelAdmin):
    """ Premium User Admin """
    list_display = (
        'user',
        'start_date',
        'end_date',
        'subscription',
    )


admin.site.register(PremiumUser, PremiumUserAdmin)
