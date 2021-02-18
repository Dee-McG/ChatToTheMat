from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>/', views.user_profile, name='user_profile'),
    path('edit_profile/<str:user>',
         views.edit_profile, name='edit_profile'),
    path('delete_profile/<str:user>',
         views.delete_profile, name='delete_profile'),
]
