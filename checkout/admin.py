from django.contrib import admin
from .models import PremiumUser


# Register your models here.
class PremiumUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'start_date',
        'end_date',
        'subscription',
    )


admin.site.register(PremiumUser, PremiumUserAdmin)
