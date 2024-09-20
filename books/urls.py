from django.urls import path
from .views import BookDetailsView, BorrowBookView, ReturnBookView

urlpatterns = [
    path("<int:id>/", BookDetailsView.as_view(), name="book_details"),
    path("borrow/<int:id>", BorrowBookView.as_view(), name="borrow_book"),
    path("return/<int:id>", ReturnBookView.as_view(), name="return_book"),
]
