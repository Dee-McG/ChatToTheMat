from django.shortcuts import render


def private_messages(request):
    """ A view to return the private messages page """

    return render(request, 'private_messages/private_messages.html')