from django.shortcuts import render


def chat_home(request):
    """ A view to return the index page """

    return render(request, 'chat_rooms/chat_home.html')