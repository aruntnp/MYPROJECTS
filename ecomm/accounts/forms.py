from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GuestEmail


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GuestForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput())

