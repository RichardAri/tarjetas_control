# Generated by Django 5.0.3 on 2024-03-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('supervisor', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('en_curso', 'En curso'), ('terminado', 'Terminado')], default='en_curso', max_length=20)),
                ('equipos_necesarios', models.ManyToManyField(to='servicios.equipo')),
            ],
        ),
    ]
