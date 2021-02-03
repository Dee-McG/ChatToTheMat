from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Chat
from .models import User
from .forms import ChatForm

def chat_home(request):
    """ A view to return the chatrooms page """
    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

    chat = Chat.objects.all()
    
    context = {
        'chat': chat,
    }

    return render(request, 'chat_rooms/chat_home.html', context)


def chat_room(request):
    chat = Chat.objects.all()
    
    context = {
        'chat': chat,
    }

    try:
        user = get_object_or_404(Chat, user=request.user)
    except Exception as e:
        user = Chat(user=request.user)

    if request.method == 'POST':

        form = ChatForm(request.POST, instance=user)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.time = datetime.now()           
            form.save()
            return redirect(reverse('chat_home'))
        else:
           messages.error(request, 'Error! Something went wrong. Your message was not sent.')
    else:
        form = ChatForm(instance=user) 
    
    return render(request, 'chat_rooms/chat_home.html', context)
