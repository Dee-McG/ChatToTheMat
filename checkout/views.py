from chat_to_the_mat.settings import STRIPE_WH_SECRET
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from dateutil.relativedelta import relativedelta

import json
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def checkout(request):
    
    return render(request, 'checkout/checkout.html')


def charge(request):
    amount = 4.99

    try:
        if request.method == 'POST':
            customer = stripe.Customer.create(
                email=request.POST['email'],
                name=request.POST['name'],
                source=request.POST['stripeToken'],
            )

            charge = stripe.Charge.create(
                customer=customer,
                amount=499,
                currency='eur',
                description='Subscription to Chat To The Mat'
            )
    except Exception as e:
        return render(request, 'checkout/checkout_error.html')
    
    return redirect(reverse('checkout_success', args=[amount]))


def checkout_success(request, args):
    amount = args
    start_date = datetime.now()
    end_date = start_date + relativedelta(years=1)
    
    start_date = datetime.strftime(start_date, '%d %B %Y')
    end_date = datetime.strftime(end_date, '%d %B %Y')

    context= {
        'start_date': start_date,
        'end_date': end_date,
        'amount': amount,
    }

    return render(request, 'checkout/checkout_success.html', context)


def checkout_error(request):
    
    return render(request, 'checkout/checkout_error.html')