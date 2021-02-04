from django.urls import path
from . import views

urlpatterns = [
    path('room/general/', views.chat_home, name='chat_home'),
    path('room/sports/', views.sports_chat, name='sports_chat'),
]