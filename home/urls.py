from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
]
