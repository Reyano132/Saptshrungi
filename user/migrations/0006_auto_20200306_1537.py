# Generated by Django 3.0.4 on 2020-03-06 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200306_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2020, 3, 6, 15, 37, 2, 894581)),
        ),
    ]
