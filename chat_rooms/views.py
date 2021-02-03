from django.shortcuts import render


def chat_home(request):
    """ A view to return the chatrooms page """
    if not request.user.is_authenticated:
        return render(request, 'home/index.html')
    
    return render(request, 'chat_rooms/chat_home.html')