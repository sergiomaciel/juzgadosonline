# Generated by Django 2.2 on 2019-05-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0019_auto_20190522_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actualizacion',
            options={'ordering': ['-fecha_publicado']},
        ),
        migrations.AlterField(
            model_name='actualizacion',
            name='fecha_publicado',
            field=models.DateField(blank=True, null=True),
        ),
    ]