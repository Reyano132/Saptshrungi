# Generated by Django 2.2.2 on 2020-01-20 16:44

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('documents', django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=3000, null=True, size=10)),
            ],
        ),
    ]
