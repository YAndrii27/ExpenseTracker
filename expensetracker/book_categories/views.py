from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from book_categories.models import BookCategory


class BookCategoryCreateView(CreateView):
    model = BookCategory
    fields = ["name"]
    success_url = "/categories/read"


class BookCategoryUpdateView(UpdateView):
    model = BookCategory
    fields = ["name"]
    success_url = "/categories/read"

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return BookCategory.objects.get(name=name)


class BookCategoryDeleteView(DeleteView):
    model = BookCategory
    success_url = "/categories/read"

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return BookCategory.objects.get(name=name)


class BookCategoryReadView(ListView):
    model = BookCategory
    paginate_by = 10
