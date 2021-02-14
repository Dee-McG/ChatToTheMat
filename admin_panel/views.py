from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from contact.models import Contact
from .forms import BanUserForm

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def admin_panel(request):
    """ View to return admin panel to superusers displaying
    Open contact queries """
    if not request.user.is_superuser:
        messages.error(request,
                       'Only admins can access the admin panel')
        return redirect(reverse('home'))

    contacts = Contact.objects.filter(
        complete=False)

    form = BanUserForm

    context = {
        'contacts': contacts,
        'form': form,
    }

    return render(request, 'admin_panel/admin_panel.html', context)


@login_required
def update_contact_status(request, contact_id):
    """ View to mark contact query as complete """
    if not request.user.is_superuser:
        messages.error(request,
                       'Only admins can update contact queries')
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, id=contact_id)

    contact.complete = True
    contact.save()

    return redirect(reverse('admin_panel'))


@login_required
def ban_user(request):
    """ View to allow admins to ban user """

    if request.method == 'POST':
        form = BanUserForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect(reverse('admin_panel'))
