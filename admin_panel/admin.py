from django.contrib import admin
from .models import BannedUsers


class BanUserAdmin(admin.ModelAdmin):
    """ Ban user admin """
    list_display = (
        'user',
        'banned',
        'reason',
    )


admin.site.register(BannedUsers, BanUserAdmin)
