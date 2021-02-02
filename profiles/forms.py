from django import forms
from .models import EditProfile


class EditProfileForm(forms.ModelForm):
    """ Form for user to edit profile that uses all fields """
    class Meta:
        model = EditProfile
        fields = ['name', 'location', 'bio']