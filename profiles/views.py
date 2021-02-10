from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EditProfileForm
from .models import UserProfile
from .models import User


# Create your views here.
@login_required
def user_profile(request, user):
    """ A view to return the profile page """

    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

    try:
        get_user = get_object_or_404(User, username=user)

        user_profile = get_object_or_404(UserProfile, user=get_user)

        context = {
                'user_profile': user_profile,
            }

        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        return render(request, 'profiles/profile.html')


@login_required
def edit_profile(request, user):
    """ A function to edit the users profile and render
    the edit_profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':

        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
        else:
            messages.error(request,
                           'Profile update failed.'
                           'Please ensure the form is valid!')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)


@login_required
def delete_profile(request):
    """ Delete current logged in user"""

    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

    user = get_object_or_404(User, pk=request.user.pk)
    try:
        user.delete()
        messages.success(request, "The user is deleted")
        return render(request, 'home/index.html')
    except Exception as e:
        messages.error(request,
                       "Something went wrong. User has not been deleted.")
        return render(request, 'profiles/profile.html')
