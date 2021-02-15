from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse

from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import PremiumUser

import stripe


# Create your views here.
@login_required
def checkout(request):
    """ A view to return the checkout page """

    return render(request, 'checkout/checkout.html')


@csrf_exempt
def stripe_config(request):
    """ Configure stripe """
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """ A view to create a checkout session using the product
    create in stripe with a price of 4.99 """
    if request.method == 'GET':
        domain_url = 'https://chat-to-the-mat.herokuapp.com/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id
                if request.user.is_authenticated else None,
                success_url=domain_url + 'checkout/success/',
                cancel_url=domain_url + 'checkout/cancel/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def cancel(request):
    """ A view to render checkout error page """
    return render(request, 'checkout/checkout_error.html')


@login_required
def success(request):
    """ A view to render the checkout success page. It gets the
    current date and adds 1 year to send to the template for start
    ad end subscription dates """

    amount = 4.99
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
def subscription_active(request):
    """ A view to render the subscription active page """

    return render(request, 'checkout/subscription_active.html')


@csrf_exempt
def stripe_webhook(request):
    """ Webhook handling, create premium user if payment is successful
    and return 200 response. Return 400 is payment is unsuccessful """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        start_date = datetime.now()
        end_date = start_date + relativedelta(years=1)

        PremiumUser.objects.create(
            user=request.user, start_date=start_date,
            end_date=end_date, subscription=True)

    return HttpResponse(status=200)
