from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from robots.serializers import RobotSerializer


@api_view(['POST'])
def create_one_robot(request):
    serializer = RobotSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
