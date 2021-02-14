from django.shortcuts import render, redirect, reverse

from contact.models import Contact
from contact.forms import ContactForm

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def admin_panel(request):
    """ View to return admin panel to superusers """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(request, 'admin_panel/admin_panel.html', context)
