from django import forms
from .models import BannedUsers


class BanUserForm(forms.ModelForm):
    """ Form for BannedUsers model to allow admins
    to ban users from posting in chat rooms """
    class Meta:
        model = BannedUsers
        fields = '__all__'
