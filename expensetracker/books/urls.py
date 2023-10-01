from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.BookCreateView.as_view(), name="create_book"),
    path("read/", views.BookCategoryReadView.as_view(), name="list_books"),
    path("update/<int:id>", views.BookCategoryUpdateView.as_view(), name="update_book"),
    path("delete/<int:id>", views.BookCategoryDeleteView.as_view(), name="delete_book")
]
