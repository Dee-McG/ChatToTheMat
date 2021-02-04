from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Chat, SportChat, User
from .forms import ChatForm, SportChatForm

def chat_home(request):
    """ A view to return the chatrooms page defaulting
    to the general chat """
    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

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
           messages.error(request, 'Error! Something went wrong. Your message was not sent.')
    else:
        form = ChatForm(instance=user) 
    
    return render(request, 'chat_rooms/chat_home.html', context)


def sports_chat(request):
    """ A view to return the chat room page using sports model """
    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

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
           messages.error(request, 'Error! Something went wrong. Your message was not sent.')
    else:
        form = SportChatForm(instance=user) 
    
    return render(request, 'chat_rooms/chat_home.html', context)