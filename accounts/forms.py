from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from wallet.models import UserWallet


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"id": "required"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"id": "required"}))
    password2 = forms.CharField(label="Confirm Password")
    usable_password = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            UserWallet.objects.create(user=our_user, balance=0)
        return our_user
