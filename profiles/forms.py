from django import forms
from .widgets import CustomClearableFileInput
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    """ Form for user to edit profile """
    class Meta:
        model = UserProfile
        fields = ['name', 'location', 'bio']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
