from django.contrib import admin
from .models import BannedUsers


# Register your models here.
class BanUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'banned',
        'reason',
    )


admin.site.register(BannedUsers, BanUserAdmin)
