from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.BookCategoryCreateView.as_view(), name="create_category"),
    path("update/<str:name>", views.BookCategoryUpdateView.as_view(), name="update_category"),
    path("read/", views.BookCategoryReadView.as_view(), name="read_categories"),
    path("delete/<str:name>", views.BookCategoryDeleteView.as_view(), name="delete_category"),
]
