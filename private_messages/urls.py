from django.urls import path
from . import views

urlpatterns = [
    path('', views.private_messages, name='private_messages'),
]