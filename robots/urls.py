from django.urls import path

from robots.views import make_week_report_to_xlsx

urlpatterns = [
    path('robots/report/xlsx/last_week', make_week_report_to_xlsx),
]