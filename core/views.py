from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from books.models import BookCategory, Books


class HomeView(ListView):
    model = Books
    template_name = "index.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_slug = self.kwargs.get("cat_slug")
        if cat_slug:
            category = get_object_or_404(BookCategory, slug=cat_slug)
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = BookCategory.objects.all()

        cat_slug = self.kwargs.get("cat_slug")
        if cat_slug:
            context["filter"] = BookCategory.objects.get(slug=cat_slug).category_name
        context["user"] = self.request.user
        return context
