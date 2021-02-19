from django.contrib import admin
from .models import ChatMessage


class ChatMessageAdmin(admin.ModelAdmin):
    """ Chat message admin """
    list_display = (
        'room',
        'user',
        'message',
        'time',
    )


admin.site.register(ChatMessage, ChatMessageAdmin)
