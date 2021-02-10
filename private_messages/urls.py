from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_private_messages, name='get_private_messages'),
    path('send_private_message/', views.send_private_message, name='send_private_message'),
]