from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('webhook/', views.stripe_webhook),
    path('subscription_active/',
         views.subscription_active, name='subscription_active'),
]
