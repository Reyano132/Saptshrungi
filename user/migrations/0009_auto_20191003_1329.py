# Generated by Django 2.2.5 on 2019-10-03 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20191003_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2019, 10, 3, 13, 29, 9, 240965)),
        ),
    ]
