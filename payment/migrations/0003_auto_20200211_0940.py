# Generated by Django 2.2.2 on 2020-02-11 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_paymentdata_for_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='dated',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 2, 11, 9, 40, 22, 188479)),
        ),
    ]