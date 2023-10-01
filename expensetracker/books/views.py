from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from books.models import Book


class BookCreateView(CreateView):
    model = Book
    fields = [
        "title", "subtitle", "authors",
        "publisher", "published_date", "distribution_expense",
        "category",
    ]
    success_url = "/books/read"


class BookCategoryUpdateView(UpdateView):
    model = Book
    fields = [
        "title", "subtitle", "authors",
        "publisher", "published_date", "distribution_expense",
        "category",
    ]
    success_url = "/books/read"

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return Book.objects.get(id=id)


class BookCategoryDeleteView(DeleteView):
    model = Book
    success_url = "/books/read"

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return Book.objects.get(id=id)


class BookCategoryReadView(ListView):
    model = Book
    paginate_by = 30
