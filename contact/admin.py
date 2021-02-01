from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_reason',
        'name',
        'email',
        'comments',
    )


admin.site.register(Contact, ContactAdmin)