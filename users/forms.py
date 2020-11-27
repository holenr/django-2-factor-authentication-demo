# users/forms.py


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Customer

class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('customer_id', 'age', 'phone_number', 'user_id',)

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields
