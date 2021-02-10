from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Chat, SportChat, User
from .forms import ChatForm, SportChatForm


@login_required
def chat_home(request):
    """ A view to return the chatrooms page defaulting
    to the general chat """
    chat = Chat.objects.all()

    channel = 'general'

    context = {
        'chat': chat,
        'channel': channel,
    }

    try:
        user = get_object_or_404(User, user=request.user)
    except Exception as e:
        user = Chat(user=request.user)

    if request.method == 'POST':

        form = ChatForm(request.POST, instance=user)
        if form.is_valid():
            # Prevent auto save and add in time field
            form = form.save(commit=False)
            form.time = datetime.now()
            form.save()

            # Count DB entries and delete oldest record
            count = Chat.objects.count()
            if count > 20:
                Chat.objects.order_by('time')[0].delete()

            return redirect(reverse('chat_home'))
        else:
            messages.error(request,
                           'Error! Something went wrong.'
                           'Your message was not sent.')
    else:
        form = ChatForm(instance=user)

    return render(request, 'chat_rooms/chat_home.html', context)


@login_required
def sports_chat(request):
    """ A view to return the chat room page using sports model """

    chat = SportChat.objects.all()

    channel = 'sports'

    context = {
        'chat': chat,
        'channel': channel,
    }

    try:
        user = get_object_or_404(User, user=request.user)
    except Exception as e:
        user = SportChat(user=request.user)

    if request.method == 'POST':

        form = SportChatForm(request.POST, instance=user)
        if form.is_valid():
            # Prevent auto save and add in time field
            form = form.save(commit=False)
            form.time = datetime.now()
            form.save()

            # Count DB entries and delete oldest record
            count = SportChat.objects.count()
            if count > 20:
                SportChat.objects.order_by('time')[0].delete()

            return render(request, 'chat_rooms/chat_home.html', context)
        else:
            messages.error(
                request,
                'Error! Something went wrong. Your message was not sent.')
    else:
        form = SportChatForm(instance=user)

    return render(request, 'chat_rooms/chat_home.html', context)


def delete_sport_message(request, chat_id):
    """ View to allow super users to delete sports chat messages """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('sports_chat'))

    message = get_object_or_404(SportChat, pk=chat_id)
    message.delete()
    messages.success(request, 'Message deleted!')
    return redirect(reverse('sports_chat'))


def delete_general_message(request, chat_id):
    """ View to allow super users to delete general chat messages """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('chat_home'))

    message = get_object_or_404(Chat, pk=chat_id)
    message.delete()
    messages.success(request, 'Message deleted!')
    return redirect(reverse('chat_home'))
