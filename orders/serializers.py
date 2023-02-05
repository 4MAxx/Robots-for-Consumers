from rest_framework import serializers
from orders.models import Order

from robots.services import is_valid_robot_model


class OrderSerializer(serializers.ModelSerializer):
    robot_serial = serializers.CharField(max_length=5, min_length=4)
    class Meta:
        model = Order
        fields = '__all__'

    def validate_robot_serial(self, value):
        if not '-' in value or value.count('-') > 1:
            raise serializers.ValidationError('Неверный формат серийного номера, =robot_serial= is Invalid')
        robot_model = value[:2]
        if not is_valid_robot_model(robot_model):
            raise serializers.ValidationError('Указанной модели робота в системе не существует!')
        return value