# Generated by Django 5.0.7 on 2024-07-19 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 19, 23, 13, 42, 975453)),
        ),
    ]
