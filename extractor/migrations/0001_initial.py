# Generated by Django 2.2 on 2019-04-30 06:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('juzgados', '0003_auto_20190430_0331'),
        ('expedientes', '0005_auto_20190430_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('ultima_fecha', models.DateTimeField(blank=True, null=True)),
                ('juzgado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='juzgados.Juzgado')),
            ],
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('encabezado', models.TextField(null=True)),
                ('separador', models.CharField(max_length=50)),
                ('nota', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogExpediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('accion', models.CharField(max_length=50)),
                ('despacho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='extractor.Despacho')),
                ('expediente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expedientes.Expediente')),
            ],
        ),
        migrations.CreateModel(
            name='LogActualizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('accion', models.CharField(max_length=50)),
                ('actualizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expedientes.Actualizacion')),
                ('despacho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='extractor.Despacho')),
            ],
        ),
        migrations.AddField(
            model_name='despacho',
            name='plantilla',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='extractor.Plantilla'),
        ),
    ]
