from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    authors = models.CharField(max_length=64)
    publisher = models.CharField(max_length=128)
    published_date = models.DateField()
    category = models.ForeignKey(
        to="book_categories.BookCategory",
        to_field="name",
        on_delete=models.CASCADE
    )
    distribution_expense = models.FloatField()
