from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

# Create your views here.
def profiles(request):
    """ A view to return the profile page """

    return render(request, 'profiles/profile.html')


def edit_profile(request):
    """ A function to edit the users profile and render the edit_profile page """
    if request.method == 'POST':

        form = EditProfileForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect(reverse('profiles'))
        else:
           messages.error(request, 'Profile update failed. Please ensure the form is valid!') 

    else: 
        form = EditProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)