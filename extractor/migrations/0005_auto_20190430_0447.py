# Generated by Django 2.2 on 2019-04-30 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0004_auto_20190430_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEspediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
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
            name='tipo',
        ),
        migrations.AddField(
            model_name='plantilla',
            name='tipos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='extractor.TipoEspediente'),
        ),
    ]
