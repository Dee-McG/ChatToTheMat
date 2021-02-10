from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

from django.contrib.auth.decorators import login_required

from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import PremiumUser

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
@login_required
def checkout(request):
    """ A view to return the checkout page """
    try:
        check_user = get_object_or_404(PremiumUser, user=request.user)
        return render(request, 'checkout/subscription_active.html')
    except Exception as e:
        return render(request, 'checkout/checkout.html')


@login_required
def charge(request):
    """ A view to charge the customer 4.99 subscription fee.
    If successful, PremiumUser will be created.
    If payment fails, render the checkout_error page otherwise
    it will redirect to the checkout page """
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

            # Create start and end dates for subscription
            start_date = datetime.now()
            end_date = start_date + relativedelta(years=1)

            # Add logged in user to PremiumUsers
            PremiumUser.objects.create(
                user=request.user, start_date=start_date,
                end_date=end_date, subscription=True)

            return redirect(reverse('checkout_success', args=[amount]))

    except Exception as e:
        return render(request, 'checkout/checkout_error.html')

    return render(request, 'checkout/checkout.html')


@login_required
def checkout_success(request, args):
    """ A view to render the checkout success page. It gets the
    current date and adds 1 year to send to the template for start
    ad end subscription dates """

    amount = args
    start_date = datetime.now()
    end_date = start_date + relativedelta(years=1)

    start_date = datetime.strftime(start_date, '%d %B %Y')
    end_date = datetime.strftime(end_date, '%d %B %Y')

    context = {
        'start_date': start_date,
        'end_date': end_date,
        'amount': amount,
    }

    return render(request, 'checkout/checkout_success.html', context)


@login_required
def checkout_error(request):
    """ A view to render the checkout error page """
    return render(request, 'checkout/checkout_error.html')


@login_required
def subscription_active(request):
    """ A view to render the subscription active page """

    return render(request, 'checkout/subscription_active.html')
