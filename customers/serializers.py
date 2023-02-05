from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Customer
        fields = '__all__'