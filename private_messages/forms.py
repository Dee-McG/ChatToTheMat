from django import forms
from .models import PrivateMessages


class PrivateMessageForm(forms.ModelForm):
    """ Form for users to send private messages """
    class Meta:
        model = PrivateMessages
        fields = ['to_user', 'message']