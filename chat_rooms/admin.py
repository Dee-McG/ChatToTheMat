from django.contrib import admin
from .models import Chat, SportChat


# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'message',
        'time',
    )


class SportChatAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'message',
        'time',
    )


admin.site.register(Chat, ChatAdmin)
admin.site.register(SportChat, SportChatAdmin)
