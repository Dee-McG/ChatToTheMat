from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact'))

    else: 
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
