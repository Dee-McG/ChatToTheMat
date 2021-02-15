from django import forms
from .widgets import CustomClearableFileInput
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    """ Form for user to edit profile that uses all fields """
    class Meta:
        model = UserProfile
        fields = ['name', 'location', 'bio']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
