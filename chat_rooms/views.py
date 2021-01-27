from django.shortcuts import render


def chat_home(request):
    """ A view to return the chatrooms page """

    return render(request, 'chat_rooms/chat_home.html')