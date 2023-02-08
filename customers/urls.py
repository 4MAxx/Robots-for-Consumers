from django.urls import path

from customers.views import CustomerCreateApi

urlpatterns = [
    path('customer/add', CustomerCreateApi.as_view(), name='create_customer'),
]