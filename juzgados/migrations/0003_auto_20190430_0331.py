# Generated by Django 2.2 on 2019-04-30 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juzgados', '0002_auto_20190430_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juzgado',
            name='actualizacion',
        ),
        migrations.RemoveField(
            model_name='juzgado',
            name='url',
        ),
    ]
