# Generated by Django 3.0.4 on 2020-03-06 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20200306_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 3, 6, 15, 45, 32, 13010)),
        ),
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 3, 6, 15, 45, 32, 13010)),
        ),
    ]