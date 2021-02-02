from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
]