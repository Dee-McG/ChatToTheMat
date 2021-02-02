from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EditProfileForm
from .models import EditProfile
from .models import User


# Create your views here.
def profiles(request):
    """ A view to return the profile page """

    try:
        profile = get_object_or_404(EditProfile, user=request.user)

        context = {
            'profile': profile,
        }

        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        return render(request, 'profiles/profile.html')



def edit_profile(request):
    """ A function to edit the users profile and render the edit_profile page """
    try:
        profile = get_object_or_404(EditProfile, user=request.user)
    except Exception as e:
        profile = EditProfile(user=request.user)
    
    if request.method == 'POST':

        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect(reverse('profiles'))
        else:
           messages.error(request, 'Profile update failed. Please ensure the form is valid!') 

    else: 
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)

def delete_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    try:
        user.delete()
        messages.success(request, "The user is deleted")
        return render(request, 'home/index.html') 
    except Exception as e:
        messages.error(request, "Something went wrong. User has not been deleted.")
        return render(request, 'profiles/profile.html')