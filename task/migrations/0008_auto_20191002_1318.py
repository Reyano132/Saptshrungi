# Generated by Django 2.2.5 on 2019-10-02 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20191002_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2019, 10, 2, 13, 18, 32, 663846)),
        ),
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2019, 10, 2, 13, 18, 32, 663846)),
        ),
    ]
