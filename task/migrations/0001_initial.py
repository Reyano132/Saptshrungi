# Generated by Django 2.2.5 on 2019-10-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=20)),
                ('progress', models.IntegerField(default=0)),
                ('due_date', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('charges', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
