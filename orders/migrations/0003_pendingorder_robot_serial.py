# Generated by Django 4.1.6 on 2023-02-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_id_pendingorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingorder',
            name='robot_serial',
            field=models.CharField(default='11-11', max_length=5),
            preserve_default=False,
        ),
    ]
