# Generated by Django 2.2 on 2019-05-06 03:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0009_auto_20190506_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='subscriptores',
            field=models.ManyToManyField(null=True, related_name='subscriptores', to=settings.AUTH_USER_MODEL),
        ),
    ]
