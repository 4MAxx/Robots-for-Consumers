from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from robots.serializers import RobotSerializer

from robots.services import get_robots_in_last_days, generate_report_xlsx_file


@api_view(['GET'])
def make_week_report_to_xlsx(request):
    robots = get_robots_in_last_days(7)
    if robots:
        xlsx_file_path = generate_report_xlsx_file(robots)
        xlsx_file = open(xlsx_file_path, mode='rb')
        response = HttpResponse(xlsx_file, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename={xlsx_file_path}'
        xlsx_file.close()
        return response
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Нет роботов в заданный период"})


@api_view(['POST'])
def create_one_robot(request):
    serializer = RobotSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
