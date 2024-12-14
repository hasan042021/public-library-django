from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, View
from books.models import BookCategory, Books


class HomeView(TemplateView):
    template_name = "index.html"
