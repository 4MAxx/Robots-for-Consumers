from rest_framework import serializers

from robots.models import Robot


def get_valid_models_list():
    ''' Список производимых моделей можно получать откуда угодно'''
    AVAILABLE_MODELS = ['R1', 'R2', 'R5', 'S1', 'S2', 'S3']
    return AVAILABLE_MODELS


def valid_model(model):
    return model in get_valid_models_list()


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
        if not valid_model(value):
            raise serializers.ValidationError('Такой модели в системе не существует!')
        return value

    def create(self, validated_data):
        validated_data['serial'] = f'{validated_data["model"]}-{validated_data["version"]}'
        return Robot.objects.create(**validated_data)
