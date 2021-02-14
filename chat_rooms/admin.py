from django.contrib import admin
from .models import ChatMessage


# Register your models here.
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'user',
        'message',
        'time',
    )


admin.site.register(ChatMessage, ChatMessageAdmin)
