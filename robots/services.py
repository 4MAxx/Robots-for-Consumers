import os

import pandas as pd
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count

from robots.models import Robot


def get_robots_in_last_days(days):
    robots = Robot.objects.filter(created__gte=timezone.now() - timedelta(days=days))
    report = robots.values('model', 'version').annotate(total=Count("id")).order_by('model')
    return list(report)


def generate_report_xlsx_file(robots_list):
    xlsx_filename = f'{os.getcwd()}/robots/reports/robot-report-{timezone.now().date()}.xlsx'
    header = ['Модель', 'Версия', 'Количество за неделю']
    robots_df = pd.DataFrame.from_dict(robots_list)
    robots_model_groups = robots_df.groupby('model')
    robots_writer = pd.ExcelWriter(xlsx_filename, engine='xlsxwriter')
    for model, model_info in robots_model_groups:
        model_info.to_excel(robots_writer, sheet_name=model, header=header, index=False)
    # for robot in robots_list:
    #     frame = pd.DataFrame([robot])
    #     frame.to_excel(robots_writer, sheet_name=robot['model'], header=header, index=False)
    robots_writer.save()
    return xlsx_filename