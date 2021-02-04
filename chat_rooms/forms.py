from django import forms
from .models import Chat, SportChat


class ChatForm(forms.ModelForm):
    """ Form for user to add a chat message, takes in message field """
    class Meta:
        model = Chat
        fields = ['message']


class SportChatForm(forms.ModelForm):
    """ Form for user to add a chat message, takes in message field """
    class Meta:
        model = SportChat
        fields = ['message']