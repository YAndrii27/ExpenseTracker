from django.urls import path

from . import views


urlpatterns = [
    path("", views.OutputTypeSelectionView.as_view(), name="selection"),
    path("charts/", views.ExpenseTrackerChartsView.as_view(), name="charts"),
    path("table/", views.ExpenseTrackerTableView.as_view(), name="table")
]
