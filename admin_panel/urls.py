from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('ban_user/', views.ban_user, name='ban_user'),
    path('contact_status/<int:contact_id>',
         views.update_contact_status, name='update_contact_status'),
]
