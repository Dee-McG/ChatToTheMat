from django import forms
from .models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    """ Form for user to add a chat message, takes in message field """
    class Meta:
        model = ChatMessage
        fields = ['message']
