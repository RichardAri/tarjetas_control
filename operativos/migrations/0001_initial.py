# Generated by Django 5.0.3 on 2024-04-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoOperativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('operativo_equipos', models.CharField(blank=True, max_length=100, null=True)),
                ('operativo_materiales', models.CharField(blank=True, max_length=100, null=True)),
                ('operativo_herramientas', models.CharField(blank=True, max_length=100, null=True)),
                ('operativo_manodeobra', models.CharField(blank=True, max_length=100, null=True)),
                ('operativo_epps', models.CharField(blank=True, max_length=100, null=True)),
                ('operativo_generales', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
