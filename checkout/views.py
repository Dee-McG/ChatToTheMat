from django.shortcuts import render

# Create your views here.
def checkout(request):
    return render(request, 'checkout/checkout.html')


def checkout_success(request):
    return render(request, 'checkout/checkout_success.html')