# Generated by Django 2.2 on 2019-04-30 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0010_auto_20190430_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipocaratula',
            old_name='nombre',
            new_name='patron',
        ),
        migrations.RemoveField(
            model_name='tipocaratula',
            name='codigo',
        ),
    ]