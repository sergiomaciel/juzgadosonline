# Generated by Django 2.2 on 2019-05-06 03:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0007_auto_20190506_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='subscriptores',
            field=models.ManyToManyField(default=None, related_name='subscriptores', to=settings.AUTH_USER_MODEL),
        ),
    ]