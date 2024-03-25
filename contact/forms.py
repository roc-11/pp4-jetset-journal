from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    """
    Form class for users to request a contact request
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
