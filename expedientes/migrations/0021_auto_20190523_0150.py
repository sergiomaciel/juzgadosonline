# Generated by Django 2.2 on 2019-05-23 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0020_auto_20190523_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualizacion',
            name='fecha_publicado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
