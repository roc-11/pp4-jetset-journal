from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form for handling updates to the user profile.

    It extends Django's ModelForm and customizes its appearance
    using crispy_formsand additional field modifications.
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'email')
