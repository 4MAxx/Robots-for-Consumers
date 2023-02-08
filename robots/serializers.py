from rest_framework import serializers

from robots.models import Robot
from robots.services import is_valid_robot_model


class RobotSerializer(serializers.ModelSerializer):
    model = serializers.CharField()
    version = serializers.CharField(max_length=2)
    created = serializers.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Robot
        fields = [
            "model",
            "version",
            "created",
        ]

    def validate_model(self, value):
        if not is_valid_robot_model(value):
            raise serializers.ValidationError('Такой модели в системе не существует!')
        return value

    def create(self, validated_data):
        validated_data['serial'] = f'{validated_data["model"]}-{validated_data["version"]}'
        return Robot.objects.create(**validated_data)
