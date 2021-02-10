from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import datetime

from .forms import PrivateMessageForm
from .models import PrivateMessages


def get_private_messages(request):
    """ A view to return the private messages page and display messages
    sent to the user """
    try:
        user = request.user.premiumuser
    except Exception as e:
        messages.error(request,
                       'Please buy a subscription'
                       'to access private messaging.')
        return redirect(reverse('checkout'))

    try:
        if request.user.premiumuser:
            private_messages = PrivateMessages.objects.filter(
                to_user=request.user)

            context = {
                'private_messages': private_messages,
            }

            return render(request,
                          'private_messages/private_messages.html', context)

    except Exception as e:
        return render(request, 'private_messages/private_messages.html')


@login_required
def send_private_message(request):
    """ A view to enable users to send private messages if
    the user has a premium subscription. Else redirect to the
    checkout page """

    try:
        if request.user.premiumuser:
            user = request.user.username

            if request.method == 'POST':

                form = PrivateMessageForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.date_time = datetime.now()
                    form.from_user = user
                    form.save()
                    messages.success(request,
                                     'Message sent! Please note, if user does'
                                     'not have a premium subscription, they'
                                     'will not see messages.')

                    return redirect(reverse('get_private_messages'))
                else:
                    messages.error(request, 'Message failed to send!')

            else:
                form = PrivateMessageForm()

            context = {
                'form': form,
            }

            return render(request,
                          'private_messages/send_private_message.html',
                          context)

    except Exception as e:
        messages.error(
            request,
            'Please buy a subscription to access private messaging.')
        return redirect(reverse('checkout'))
