from typing import Any
from django import forms
from .models import UserWallet


class DepositForm(forms.ModelForm):

    class Meta:
        model = UserWallet
        fields = ["amount"]

    def save(self, commit=True):

        return super().save(commit)
