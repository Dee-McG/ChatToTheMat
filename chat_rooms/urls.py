from django.urls import path
from . import views

urlpatterns = [
    path('room/general/', views.chat_home, name='chat_home'),
    path('room/sports/', views.sports_chat, name='sports_chat'),
    path('delete/sport/<int:chat_id>/',
         views.delete_sport_message, name='delete_sport_message'),
    path('delete/general/<int:chat_id>/',
         views.delete_general_message, name='delete_general_message'),
]
