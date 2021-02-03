from django import forms
from .models import Chat


class ChatForm(forms.ModelForm):
    """ Form for user to add a chat message, takes in message field """
    class Meta:
        model = Chat
        fields = ['message']