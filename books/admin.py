from django.contrib import admin
from .models import BookCategory, Books, BorrowBook, BookReview


# Register your models here.
class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}
    list_display = ["category_name", "slug"]


admin.site.register(BookCategory, CatAdmin)
admin.site.register(Books)
admin.site.register(BorrowBook)
admin.site.register(BookReview)
