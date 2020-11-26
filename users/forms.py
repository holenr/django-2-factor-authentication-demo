# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',) # old ch 9 (default)
        fields = ('username', 'email', 'age',) # new ch 9


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields # old ch 9 (default)
        fields = ('username', 'email', 'age',) # new ch 9