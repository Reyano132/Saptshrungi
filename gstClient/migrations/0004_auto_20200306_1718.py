# Generated by Django 3.0.4 on 2020-03-06 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_isgst_service'),
        ('gstClient', '0003_auto_20200306_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsttype',
            name='gst_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service'),
        ),
    ]
