from django.urls import path

from robots.views import make_week_report_to_xlsx
from robots.views import create_one_robot


urlpatterns = [
    path('report/xlsx/last_week', make_week_report_to_xlsx),
    path('one', create_one_robot),
]