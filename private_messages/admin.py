from django.contrib import admin
from .models import PrivateMessages


# Register your models here.
class PrivateMessageAdmin(admin.ModelAdmin):
    list_display = (
        'from_user',
        'to_user',
        'date_time',
        'message',
    )


admin.site.register(PrivateMessages, PrivateMessageAdmin)
