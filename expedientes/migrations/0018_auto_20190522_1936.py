# Generated by Django 2.2 on 2019-05-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0017_auto_20190522_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='fecha_publicado',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]