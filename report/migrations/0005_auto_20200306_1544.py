# Generated by Django 3.0.4 on 2020-03-06 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20200306_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdata',
            name='from_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 3, 6, 15, 44, 11, 232690)),
        ),
        migrations.AlterField(
            model_name='reportdata',
            name='to_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 3, 6, 15, 44, 11, 232690)),
        ),
    ]
