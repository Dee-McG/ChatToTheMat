from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.checkout_success, name='checkout_success'),
    path('error/', views.checkout_error, name='checkout_error'),
]