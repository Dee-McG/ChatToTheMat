from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:room>', views.chat, name='chat'),
    path('delete_message/<str:room>/<int:chat_id>/',
         views.delete_message, name='delete_message'),
    path('banned/', views.banned, name='banned'),
]
