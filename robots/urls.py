from django.urls import path

from robots.views import create_one_robot

urlpatterns = [
    path('robots/one', create_one_robot),
]