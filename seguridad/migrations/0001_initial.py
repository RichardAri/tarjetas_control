# Generated by Django 5.0.3 on 2024-04-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoSeguridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase_seguridad', models.CharField(blank=True, max_length=100, null=True)),
                ('seguridad_peligro', models.CharField(blank=True, max_length=100, null=True)),
                ('seguridad_riesgo', models.CharField(blank=True, max_length=100, null=True)),
                ('seguridad_control', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
