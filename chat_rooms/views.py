from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import ChatMessage
from admin_panel.models import BannedUsers

from .forms import ChatMessageForm


@login_required
def chat(request, room):
    """ View to return chat messages dependent on room.
    Filters messages and counts. If message per room > 20,
    deletes the oldest message """
    banned_status = BannedUsers.objects.filter(user=request.user, banned=True)

    # Return banned if user has been banned from chat
    if banned_status:
        return redirect(reverse('banned'))

    chat = ChatMessage.objects.filter(room=room)
    user = request.user

    context = {
        'chat': chat,
        'channel': room,
        'user': user,
    }

    if request.method == 'POST':

        form = ChatMessageForm(request.POST)
        if form.is_valid():
            # Prevent auto save and add in time/user/room fields
            form = form.save(commit=False)
            form.user = user
            form.room = room
            form.time = datetime.now()
            form.save()

            # Count DB entries and delete oldest record
            count = ChatMessage.objects.filter(room=room).count()
            if count > 20:
                ChatMessage.objects.filter(
                    room=room).order_by('time')[0].delete()

            return render(request, 'chat_rooms/chat_home.html', context)
        else:
            messages.error(
                request,
                'Error! Something went wrong. Your message was not sent.')
    else:
        form = ChatMessageForm()

    return render(request, 'chat_rooms/chat_home.html', context)


def delete_message(request, room, chat_id):
    """ View to allow super users to delete chat messages """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('chat', args=[room]))

    message = get_object_or_404(ChatMessage, pk=chat_id)
    message.delete()
    messages.success(request, 'Message deleted!')
    return redirect(reverse('chat', args=[room]))


@login_required
def banned(request):
    return render(request, 'chat_rooms/banned.html')
