# Generated by Django 2.2 on 2019-04-30 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0004_auto_20190428_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='fecha_creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
