from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """ User Pforile admin """
    list_display = (
        'user',
        'name',
        'location',
        'bio',
    )


admin.site.register(UserProfile, UserProfileAdmin)
