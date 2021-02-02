from django.contrib import admin
from .models import EditProfile

# Register your models here.
class EditProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'location',
        'bio',
    )


admin.site.register(EditProfile, EditProfileAdmin)