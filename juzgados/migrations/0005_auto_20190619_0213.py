# Generated by Django 2.2 on 2019-06-19 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juzgados', '0004_delegado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegado',
            name='creado',
            field=models.DateField(default=datetime.datetime(2019, 6, 19, 2, 13, 34, 829798)),
        ),
    ]