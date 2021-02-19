from django.contrib import admin
from .models import PrivateMessages


class PrivateMessageAdmin(admin.ModelAdmin):
    """ Private message admin """
    list_display = (
        'from_user',
        'to_user',
        'date_time',
        'message',
    )


admin.site.register(PrivateMessages, PrivateMessageAdmin)
