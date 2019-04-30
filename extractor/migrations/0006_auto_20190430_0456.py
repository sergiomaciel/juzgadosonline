# Generated by Django 2.2 on 2019-04-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0005_auto_20190430_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCaratula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30, unique=True)),
                ('caratula', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=100, null=True)),
                ('demandado', models.CharField(max_length=100, null=True)),
                ('causa', models.CharField(max_length=200, null=True)),
                ('nota', models.TextField(max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='plantilla',
            name='tipos',
        ),
        migrations.DeleteModel(
            name='TipoEspediente',
        ),
        migrations.AddField(
            model_name='plantilla',
            name='tipos_de_caratulas',
            field=models.ManyToManyField(related_name='tipos_de_caratulas', to='extractor.TipoCaratula'),
        ),
    ]
