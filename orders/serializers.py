from rest_framework import serializers
from orders.models import Order
from orders.services import create_pending_order

from robots.services import is_valid_robot_model, is_robot_in_stock


class OrderSerializer(serializers.ModelSerializer):
    robot_serial = serializers.CharField(max_length=5, min_length=4)

    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'robot_serial',
        ]

    def validate_robot_serial(self, value):
        if not '-' in value or value.count('-') > 1:
            raise serializers.ValidationError('Неверный формат серийного номера, =robot_serial= is Invalid')
        robot_model = value[:2]
        if not is_valid_robot_model(robot_model):
            raise serializers.ValidationError('Указанной модели робота в системе не существует!')
        return value

    def create(self, validated_data):
        if is_robot_in_stock(validated_data['robot_serial']):
            return Order.objects.create(**validated_data)
        else:
            order = Order.objects.create(**validated_data)
            create_pending_order(order.pk, order.robot_serial)
            return order