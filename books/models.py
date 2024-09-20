from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.category_name}"


class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="book_images/")
    # Adjust the upload directory as needed
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(BookCategory, related_name="category")

    def __str__(self):
        return f"{self.title} - {self.borrowing_price}"


class BorrowBook(models.Model):
    book = models.ForeignKey(Books, related_name="borrow", on_delete=models.CASCADE)
    borrower = models.ForeignKey(
        User, related_name="borrower", on_delete=models.SET_NULL, null=True
    )
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now() + timezone.timedelta(days=60))
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower}"


class BookReview(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="review")
    name = models.CharField(max_length=50)
    body = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
