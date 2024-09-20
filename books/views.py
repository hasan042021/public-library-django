from typing import Any
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BorrowBook, Books
from django.contrib import messages
from .forms import ReviewForm
from django.urls import reverse
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.
class BorrowBookView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        book_id = self.kwargs.get("id")
        book = get_object_or_404(Books, pk=book_id)
        user = request.user
        user_wallet = user.wallet
        balance = user_wallet.balance
        borrow_price = book.borrowing_price
        print("line 25")
        if balance >= borrow_price:
            print("here")
            # Create the BorrowBook object with the retrieved book and the current user
            BorrowBook.objects.create(book=book, borrower=request.user)
            user_wallet.balance -= borrow_price
            user_wallet.save()
            message = render_to_string(
                "messages/borrow_message.html",
                {"user": self.request.user, "amount": borrow_price, "book": book.title},
            )
            send_email = EmailMultiAlternatives(
                "Deposit Message", "", to=[self.request.user.email]
            )
            send_email.attach_alternative(message, "text/html")
            send_email.send()
            return redirect("home")
        else:
            print("line 34")
            messages.error(
                self.request, f"You have not sufficient balance to buy this book."
            )
            return redirect(reverse("book_details", kwargs={"id": book_id}))


class BookDetailsView(LoginRequiredMixin, DetailView):
    model = Books
    pk_url_kwarg = "id"
    template_name = "books.html"
    context_object_name = "book"

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(data=self.request.POST)
        book = self.get_object()
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        reviews = book.review.all()
        review_form = ReviewForm()
        exists = BorrowBook.objects.filter(
            book=book, borrower=self.request.user
        ).exists()
        context["reviews"] = reviews
        if exists:
            context["review_form"] = review_form

        else:
            context["review_form"] = None
        return context


class ReturnBookView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        borrow_id = kwargs.get("id")
        borrow_book = get_object_or_404(BorrowBook, pk=borrow_id)

        # Update the returned status
        borrow_book.returned = True
        borrow_book.save()

        # Update the user's balance (assuming you have a balance field in your User model)
        user_wallet = borrow_book.borrower.wallet
        user_wallet.balance += borrow_book.book.borrowing_price
        user_wallet.save()

        return redirect("profile")
