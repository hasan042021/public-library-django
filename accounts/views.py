from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, TemplateView, View, ListView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import BorrowBook

# Create your views here.


class UserRegistrationView(FormView):
    template_name = "registration.html"
    form_class = UserRegistrationForm

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("home")


class UserProfile(LoginRequiredMixin, ListView):
    template_name = "profile.html"
    model = BorrowBook
    context_object_name = "borrow_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(borrower=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
