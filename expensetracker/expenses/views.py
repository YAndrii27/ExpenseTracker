from typing import Any

from django.http import HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.db.models import Count, F, Sum
from django.shortcuts import render
from django.views import View

from .forms import SelectOutputTypeForm
from . import visualisation
from books.models import Book

csrf_protected_method = method_decorator(csrf_protect)


class OutputTypeSelectionView(View):
    def get(self, request: HttpRequest):
        return render(
            request=request,
            template_name="expenses/selector.html",
            context={"form": SelectOutputTypeForm()}
        )

    @csrf_protected_method
    def post(self, request: HttpRequest):
        form = SelectOutputTypeForm(request.POST)
        if form.is_valid():
            data: dict[str, Any] = form.cleaned_data
            return HttpResponseRedirect(f"/expenses/{data['choise']}/")
        return render(
            request=request,
            template_name="selector.html",
            context={"form": form}
        )


class ExpenseTrackerTableView(View):
    def get(self, request: HttpRequest):
        expenses = Book.objects \
            .values("category__name") \
            .annotate(
                total_books=Count("id"),
                distribution_expense=Sum(F("distribution_expense"))
            )
        formatted_data = visualisation.formatData(data=expenses)
        return render(
            request=request,
            template_name="expenses/expenses.html",
            context={"table_data": formatted_data}
        )


class ExpenseTrackerChartsView(View):
    def get(self, request: HttpRequest):
        expenses = Book.objects \
            .all() \
            .values("category__name") \
            .annotate(
                total_books=Count("id"),
                distribution_expense=Sum(F("distribution_expense"))
            )
        chart_path = visualisation.charts(expenses)
        return render(
            request=request,
            template_name="expenses/expenses.html",
            context={"chart_path": str(chart_path)}
        )
