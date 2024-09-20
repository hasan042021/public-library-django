from django.shortcuts import render, redirect
from .forms import DepositForm
from django.views.generic import FormView, CreateView
from .models import UserWallet
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.
class DepositMoneyView(LoginRequiredMixin, FormView):
    model = UserWallet
    template_name = "deposit_money.html"
    form_class = DepositForm

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        wallet = self.request.user.wallet
        wallet.balance += amount
        wallet.save()
        message = render_to_string(
            "messages/deposit_message.html",
            {
                "user": self.request.user,
                "amount": amount,
            },
        )
        send_email = EmailMultiAlternatives(
            "Deposit Message", "", to=[self.request.user.email]
        )
        send_email.attach_alternative(message, "text/html")
        send_email.send()
        return super().form_valid(form)
