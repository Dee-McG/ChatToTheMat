from django.shortcuts import render
from checkout.views import check_premium_status

def index(request):
    """ A view to return the index page and check 
    premium users to remove when end date is reached """
    check_premium_status()
    return render(request, 'home/index.html')
