from django.shortcuts import render

# Create your views here.
def profiles(request):
    """ A view to return the profile page """

    return render(request, 'profiles/profile.html')