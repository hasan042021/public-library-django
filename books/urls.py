from django.urls import path
from .views import BookDetailsView, BorrowBookView, ReturnBookView, CollectionView

urlpatterns = [
    path(
        "category/<slug:cat_slug>/", CollectionView.as_view(), name="category_wise_post"
    ),
    path("collection/", CollectionView.as_view(), name="collection"),
    path("<int:id>/", BookDetailsView.as_view(), name="book_details"),
    path("borrow/<int:id>", BorrowBookView.as_view(), name="borrow_book"),
    path("return/<int:id>", ReturnBookView.as_view(), name="return_book"),
]
