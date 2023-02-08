from django.urls import path

from orders.views import OrderCreateApi

urlpatterns = [
    path('order/add', OrderCreateApi.as_view(), name='create_order'),
]