from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('contact_status/<int:contact_id>',
         views.update_contact_status, name='update_contact_status'),
]
