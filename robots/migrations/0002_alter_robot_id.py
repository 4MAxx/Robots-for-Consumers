# Generated by Django 4.1.6 on 2023-02-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
