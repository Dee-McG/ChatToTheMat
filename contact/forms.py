from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for Contact model that uses all fields except complete """
    class Meta:
        model = Contact
        fields = ['contact_reason', 'name', 'email', 'comments']
